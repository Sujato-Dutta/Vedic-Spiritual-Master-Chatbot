# Streamlit Cloud Deployment Guide

## Prerequisites
1. GitHub repository with your code pushed
2. Google API Key

## Deployment Steps

### 1. Deploy to Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository: `vedic-spiritual-master-chatbot`
5. Set Main file path: `app.py`
6. Click "Deploy"

### 2. Configure Secrets
Before the app runs successfully, you need to add your API key:

1. In your deployed app, click on "⋮" (three dots) in the bottom right
2. Click "Settings"
3. Go to the "Secrets" tab
4. Add the following content:
   ```toml
   GOOGLE_API_KEY = "your_actual_api_key_here"
   ```
5. Click "Save"

### 3. Important Notes
- **DO NOT** commit your `.env` file to GitHub (it's already in `.gitignore`)
- The `chroma_db` folder is also excluded from git (it will be regenerated on first run)
- You'll need to run `ingest_data.py` on Streamlit Cloud to create the vector database

### 4. Running Data Ingestion on Cloud
Since `chroma_db` is not in git, you have two options:

**Option A: Pre-commit the database (Not Recommended)**
- Remove `chroma_db/` from `.gitignore`
- Commit and push the database
- This increases repo size significantly

**Option B: Use Streamlit Cloud Shell (Recommended)**
1. After deployment, click "Manage app"
2. Open the terminal/shell
3. Run: `python ingest_data.py`
4. Wait for completion
5. Restart the app

## Troubleshooting
- If you see module errors, ensure `requirements.txt` has all dependencies with correct versions
- If API key errors occur, verify the secret is set correctly in Streamlit Cloud settings
