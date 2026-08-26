To Deploy Ngnix Image as a Pod
1. `brew install minikube`

2. `minkube start`

3. `kubectl run hello-k8s --image=nginx --port=80`

4. `kubectl get pods`

5. `kubectl expose pod hello-k8s --type=NodePort --port=80`

6. `minikube service hello-k8s`

Output: 

<img width="853" height="240" alt="Screenshot 2026-08-22 at 11 40 50 AM" src="https://github.com/user-attachments/assets/e2a96a4a-ba73-406e-bc38-58e73bdadb19" />

<img width="1014" height="621" alt="Screenshot 2026-08-22 at 11 41 11 AM" src="https://github.com/user-attachments/assets/e3ed2b5a-dcbb-4f72-960e-6d9181155811" />
