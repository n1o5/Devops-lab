
import docker
from docker.errors import NotFound

client = docker.from_env()

IMAGE_NAME = "flask-apparmor"
CONTAINER_NAME = "flask-secure-sdk"


def main():
    print("Building Docker image...")

    client.images.build(
        path=".",
        tag=IMAGE_NAME,
    )

    print("Image built successfully.")

    # Remove the previous container if it exists.
    try:
        old = client.containers.get(CONTAINER_NAME)
        old.remove(force=True)
        print("Removed previous container.")
    except NotFound:
        pass

    print("Starting secured Flask container...")

    container = client.containers.run(
        IMAGE_NAME,
        name=CONTAINER_NAME,
        ports={"5000/tcp": 5001},
        read_only=True,
        tmpfs={
            "/tmp": "rw,noexec,nosuid,size=16m"
        },
        cap_drop=["ALL"],
        security_opt=["no-new-privileges:true"],
        detach=True,
    )

    print(f"Container started: {container.short_id}")

    # Inspect the configuration.
    info = client.api.inspect_container(container.id)
    host = info["HostConfig"]

    print("\n--- Security Verification ---")
    print("Read-only root filesystem:", host["ReadonlyRootfs"])
    print("Dropped capabilities:", host["CapDrop"])
    print("Security options:", host["SecurityOpt"])
    print("AppArmor profile reported:", info.get("AppArmorProfile"))

    print("\nFlask URL: http://localhost:5001/")
    print("Run python test_restricted_actions.py next.")
    print("The container will remain running.")


if __name__ == "__main__":
    main()
