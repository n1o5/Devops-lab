## 1. Install Jenkins using Docker
```
docker run -d --name jenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts
```

Output
```
f7818bf11949a37b3f4e7db02b661fa1d15715d760bd4ce52186e7fe26e4b666
```

## 2. Get Jenkins Initial Password
```
docker ps -a
```
output
```
f7818bf11949
```
```
docker exec -it f7818bf11949 bash
jenkins@f7818bf11949:/$ cat /var/jenkins_home/secrets/initialAdminPassword
```
output
```
6ebed22656d84841b50dd3062d39b87a
```
## 3. Access Jenkins on Port 8080
http://localhost:8080/
