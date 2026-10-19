## Files

- `app.py` — serves `Hello from Flask on Kubernetes!`
- `Dockerfile` — builds the Flask app image.
- `flask_deployment.yaml` — defines a one-replica Deployment and a NodePort Service.

## Prerequisites

Install Docker, Minikube, and `kubectl`.

## Run the app

Start Minikube:

```bash
minikube start
```

Build the image in Minikube's Docker environment:

```bash
eval $(minikube docker-env)
docker build -t flask-app .
```

Apply the Kubernetes configuration:

```bash
kubectl apply -f flask_deployment.yaml
```

Check the deployment and pod:

```bash
kubectl get deployments
kubectl get pods
kubectl get services
```

Expose the service locally and test it. Keep this terminal running while using the generated URL:

```bash
minikube service flask-app-service --url
```

In a second terminal, use the URL printed by the command:

```bash
curl http://127.0.0.1:<PORT>
```

The expected response is:

```text
Hello from Flask on Kubernetes!
```

The port in the URL is assigned by Minikube and may change between runs.

## Stop / cleanup

Stop the cluster:

```bash
minikube stop
```

Delete the deployment and service:

```bash
kubectl delete -f flask_deployment.yaml
```
"""
