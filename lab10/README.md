These commands assume the project files have been created. 

## 1. Start a three-node cluster
Stop or delete an old cluster only if you no longer need its resources. Then run:

```bash
minikube stop
minikube delete
minikube start --driver=docker --nodes=3 -p devops-multinode
```

Check the cluster:

```bash
minikube -p devops-multinode status
kubectl config use-context devops-multinode
kubectl get nodes -o wide
```

## 2. Build and load the images into Minikube

Build the images from the directory containing these files:

```bash
docker build -t product-catalog:latest -f Dockerfile.product .
docker build -t shopping-cart:latest -f Dockerfile.shopping .
docker images
```

```bash
minikube -p devops-multinode image load product-catalog:latest
minikube -p devops-multinode image load shopping-cart:latest
minikube -p devops-multinode ssh -- docker images
```

## 3. Apply the manifests and verify
Run these commands from the directory containing the four YAML files:

```bash
kubectl apply -f product_catalog_deployment.yaml
kubectl apply -f shopping_cart_deployment.yaml
kubectl apply -f product_catalog_service.yaml
kubectl apply -f shopping_cart_service.yaml
```

Wait for the Deployments:

```bash
kubectl rollout status deployment/product-catalog
kubectl rollout status deployment/shopping-cart
```

Inspect replicas, pods, and node assignments:

```bash
kubectl get deployments
kubectl get pods -o wide
kubectl get services
```

Expected ready replica counts are `2/2` for `product-catalog` and `3/3` for `shopping-cart`. The `NODE` column shows which cluster node hosts each pod.

## 4. Access the services on macOS
Open a separate Terminal window for each service and leave the command running while testing. With Minikube’s Docker driver on macOS, `minikube service` may create a local tunnel and print a `127.0.0.1` URL.

Terminal 1:

```bash
minikube -p devops-multinode service product-catalog-service
```

Terminal 2:

```bash
minikube -p devops-multinode service shopping-cart-service
```

Use the exact URLs printed by your commands. Ports may be different on each run. Keep both tunnel terminals open while you test.

## 5. Test Product Catalog
Replace `<PRODUCT_URL>` with the URL printed for `product-catalog-service`:

```bash
curl <PRODUCT_URL>/products
```

Expected JSON:

```json
[
  {"id": 1, "name": "Laptop", "price": 1200},
  {"id": 2, "name": "Phone", "price": 800},
  {"id": 3, "name": "Headphones", "price": 150}
]
```

## 6. Test Shopping Cart
Replace `<CART_URL>` with the URL printed for `shopping-cart-service`.

Retrieve the cart:

```bash
curl <CART_URL>/cart
```

A newly started cart process should return:

```json
[]
```

Add an item:

```bash
curl -X POST <CART_URL>/cart \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "name": "Laptop", "quantity": 1}'
```
