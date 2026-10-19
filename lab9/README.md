These commands assume the project files have been created. 

## 1. Ensure Python is available in Jenkins
If Jenkins runs in Docker, build the custom image from the directory containing the Dockerfile:

```bash
docker build -t jenkins-python:lts -f Dockerfile .
```
To inspect a running container temporarily:

```bash
docker ps
docker exec -it -u root <jenkins-container-name-or-id> bash
python3 --version
python3 -m venv --help
```

Installing packages manually in a running container may not persist if it is replaced; a custom image is more repeatable.

## 2. Create the Jenkins Pipeline job
1. Open Jenkins, for example `http://localhost:8080`.
2. Click **New Item**.
3. Name the job `Python-MultiStage-Pipeline`.
4. Select **Pipeline**, then click **OK**.
5. Under **Pipeline**, set **Definition** to **Pipeline script from SCM**.
6. Select **Git** and enter:

   ```text
   https://github.com/<your-GitHub-username>/devops-sample-code.git
   ```
7. Set the branch to `refs/heads/main`
8. Keep **Script Path** as `Jenkinsfile`, then save.

## 3. Run and verify
Click **Build Now**, open the build, and select **Console Output**. Confirm that all five stages complete. Expected final output includes:

```text
Pipeline completed successfully!
Finished: SUCCESS
```