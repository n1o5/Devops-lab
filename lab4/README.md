## 1. Create and inspect the bridge network

```bash
docker network create --driver bridge my-bridge-net
docker network ls
docker network inspect my-bridge-net
```

## 2. Build the Flask image

Run this from the directory containing the Flask app and Dockerfile:

```bash
docker build -t flask-api .
```

## 3. Start the containers

```bash
docker run -d --name mysql --network my-bridge-net -e MYSQL_ROOT_PASSWORD=change-me mysql:latest
docker run -d --name redis --network my-bridge-net redis:latest
docker run -d --name flask --network my-bridge-net -p 5001:5001 flask-api
```

Replace `change-me` with a password of your choice. The MySQL password is configured for the container; the exercise focuses on network connectivity.

## 4. Test the Flask API

```bash
curl http://127.0.0.1:5001/about
```

The endpoint returns JSON describing the Simple REST API.

## 5. Test container connectivity

Open a shell in the Flask container:

```bash
docker exec -it flask bash
```

From inside the container, run:

```bash
ping -c 3 mysql
ping -c 3 redis
```
