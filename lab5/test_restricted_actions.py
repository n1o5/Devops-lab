
import docker
from docker.errors import NotFound

client = docker.from_env()
CONTAINER_NAME = "flask-secure-sdk"


def test_action(container, description, command):
    print(f"\n--- {description} ---")

    try:
        result = container.exec_run(command)

        print("Exit code:", result.exit_code)

        output = result.output.decode(
            "utf-8", errors="replace"
        ).strip()

        print("Output:", output if output else "(empty)")

        if result.exit_code == 0:
            print("Result: Command succeeded.")
        else:
            print("Result: Command failed or was restricted.")

    except docker.errors.APIError as error:
        print("Docker execution error:", error)


def main():
    try:
        container = client.containers.get(CONTAINER_NAME)
    except NotFound:
        print("Container not found. Run apply_apparmor.py first.")
        return

    container.reload()

    if container.status != "running":
        print("Container is not running. Start it first.")
        return

    test_action(
        container,
        "Test 1: Read /etc/passwd",
        ["cat", "/etc/passwd"],
    )

    test_action(
        container,
        "Test 2: Write to /etc",
        [
            "python",
            "-c",
            "open('/etc/lab-test.txt', 'w').write('test')",
        ],
    )

    test_action(
        container,
        "Test 3: Execute a script from /tmp",
        [
            "sh",
            "-c",
            "printf '#!/bin/sh\\necho executed\\n' "
            "> /tmp/test.sh && chmod +x /tmp/test.sh "
            "&& /tmp/test.sh",
        ],
    )

    test_action(
        container,
        "Test 4: Execute /bin/bash",
        ["/bin/bash", "-c", "echo executed"],
    )

    print("\nAll tests completed.")
    print("Flask is still running at http://localhost:5001/")


if __name__ == "__main__":
    main()
