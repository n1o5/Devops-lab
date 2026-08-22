To Deploy Ngnix Image as a Pod
1. `brew install minikube`

2. `minkube start`

3. `kubectl run hello-k8s --image=nginx --port=80`

4. `kubectl get pods`

5. `kubectl expose pod hello-k8s --type=NodePort --port=80`

6. `minikube service hello-k8s`
