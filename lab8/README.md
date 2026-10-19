
## 1. Create a GitHub repository
Name it `devops-sample-code`, set it to **Public**, and create it.

## 2. Create the shell script on macOS
In Terminal:

```bash
mkdir -p lab8
cd lab8
touch hello-world.sh
```

Put the following in `hello-world.sh`:

```bash
#!/bin/bash
echo "Hello, Jenkins!"
```

Save the file, then run:

```bash
chmod +x hello-world.sh
./hello-world.sh
```

Expected output: `Hello, Jenkins!`

## 3. Initialize Git and commit the file
If you have not configured Git before, set your identity:

```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

Then run:

```bash
git init
git add hello-world.sh
git status
git commit -m "Add hello-world.sh"
git branch -M main
```

## 4. Push the script to GitHub
Replace `<your-GitHub-username>` with your username:

```bash
git remote add origin https://github.com/<your-GitHub-username>/devops-sample-code.git
git push -u origin main
```
Verify that `hello-world.sh` appears in the GitHub repository.

## 5. Create the Jenkins Freestyle job
1. Open Jenkins, such as `http://localhost:8080`, and sign in.
2. Click **New Item**.
3. Enter `HelloWorld` as the job name.
4. Select **Freestyle project**, then click **OK**.
5. Under **Source Code Management**, select **Git**. Use the repository URL.
   ```text
   https://github.com/<your-GitHub-username>/devops-sample-code.git
   ```
6. Use `refs/heads/main` as branch name. 
7. Under **Build Steps**, select **Add build step → Execute shell**.
8. Enter:

   ```bash
   sh hello-world.sh
   ```

9. Click **Save**.

## 6. Run the job and view its output
Open the `HelloWorld` job and click **Build Now**.

output:

```text
Hello, Jenkins!
Finished: SUCCESS
```