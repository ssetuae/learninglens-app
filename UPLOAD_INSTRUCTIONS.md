# GitHub Upload Instructions for LearningLens Application

This document provides step-by-step instructions for uploading the LearningLens application code to your GitHub repository.

## Repository Information

- **Repository URL**: https://github.com/ssetuae/learninglens-app
- **Repository Name**: learninglens-app
- **Account**: ssetuae (helpdesk@shiningstaronline.com)

## Option 1: Upload via GitHub Web Interface

1. **Navigate to your repository**: Go to https://github.com/ssetuae/learninglens-app
2. **Upload files**: 
   - Click on "Add file" > "Upload files" in the repository
   - Drag and drop the files from the extracted zip archive or click to select files
   - You can upload multiple files at once, but may need to do this in batches if there are many files
   - Add a commit message like "Initial upload of LearningLens application"
   - Click "Commit changes"

## Option 2: Clone and Push via Command Line (if you have Git installed locally)

1. **Clone the repository**:
   ```
   git clone https://github.com/ssetuae/learninglens-app.git
   ```

2. **Copy files**:
   - Extract the zip archive
   - Copy all files into the cloned repository folder

3. **Commit and push**:
   ```
   cd learninglens-app
   git add .
   git commit -m "Initial upload of LearningLens application"
   git push
   ```

## Connecting to Render

After uploading the code to GitHub, you can connect Render to your GitHub repository:

1. **Log in to Render**: Use your Render account credentials
2. **Create a new Web Service**: 
   - Click "New" > "Web Service"
   - Connect your GitHub repository (ssetuae/learninglens-app)
   - Name your service (e.g., "learninglens")
   - Select the "Python 3" environment
   - Set the build command: `pip install -r requirements.txt`
   - Set the start command: `gunicorn app:app`
   - Choose the free tier
   - Click "Create Web Service"

3. **Access your deployed application**:
   - Render will provide a URL for your application (e.g., learninglens.onrender.com)
   - The initial deployment may take a few minutes to complete

## Need Help?

If you encounter any issues during the upload or deployment process, please refer to:
- [GitHub documentation on file upload](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)
- [Render documentation on deploying from GitHub](https://render.com/docs/deploy-from-github)
