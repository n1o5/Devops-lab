## Build and deploy

Start Minikube and configure Docker to use Minikube's Docker environment:

```bash
minikube start --nodes=1
eval $(minikube docker-env)
```

Build the image using the name referenced in the ReplicaSet manifest, then apply the configuration:

```bash
docker build -t flashsale:1.0 .
kubectl apply -f flashsale_replicaset.yaml
```

## Verify the ReplicaSet and Pods

```bash
kubectl get rs
kubectl get pods
kubectl get pods -o wide
kubectl get services
```

The initial configuration requests three replicas.

## Scale to five replicas

```bash
kubectl scale rs flashsale-rs --replicas=5
kubectl get rs
kubectl get pods
```

Kubernetes should create two additional Pods to reach five replicas.

## Test automatic Pod replacement

Delete one of the Pods:

```bash
kubectl delete pod <pod-name>
kubectl get pods
```

The ReplicaSet should create a replacement Pod to maintain the desired count.

## Access the application

The manifest defines a `ClusterIP` Service. Forward its port to your local machine:

```bash
kubectl port-forward service/flashsale-svc 8080:80
```

In another terminal, test the endpoints:

```bash
curl http://127.0.0.1:8080/
curl "http://127.0.0.1:8080/buy?user=123"
curl http://127.0.0.1:8080/health
```

## Clean up

```bash
kubectl delete -f flashsale_replicaset.yaml
```