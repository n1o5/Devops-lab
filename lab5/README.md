# lab 5 - MacOS version

These commands assume the five project files (`app.py`, `requirements.txt`, `Dockerfile`, `apply_apparmor.py`, and `test_restricted_actions.py`) have already been created in `~/docker-apparmor-lab`.

## 1. Create and activate the Python virtual environment to install docker sdk

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install docker
```

## 2. Build the Docker image

```bash
docker build -t flask-apparmor .
```

## 3. Start the container and inspect its security settings

```bash
python apply_apparmor.py
```

## 4. Test the Flask application

```bash
curl http://localhost:5001/
```

Expected response:

```text
Hello, this is a secure Flask application running inside a Docker container!
```

## 5. Run the restricted-action tests

Keep Docker Desktop running. In the project directory, activate the environment if needed, then run:

```bash
cd ~/docker-apparmor-lab
source .venv/bin/activate
python test_restricted_actions.py
```

## 6. Stop and remove the container

```bash
docker rm -f flask-secure-sdk
```

remove the image as well 

```bash
docker rmi flask-apparmor
```



