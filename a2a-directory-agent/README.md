Agent which interacts with MCP directory server. Assumes that the directory server is running.

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn agent:a2a_app
```

```
cd a2a-directory-agent
export PROJECT_ID=$(gcloud config get-value project)
export PROJECT_NUMBER=$(gcloud projects list --filter="$(gcloud config get-value project)" --format="value(PROJECT_NUMBER)")
gcloud builds submit . --tag=us-central1-docker.pkg.dev/$PROJECT_ID/springfield/a2a-directory-agent

gcloud run deploy a2a-directory-agent \
  --image=us-central1-docker.pkg.dev/$PROJECT_ID/springfield/a2a-directory-agent:latest \
  --region=us-central1 \
  --allow-unauthenticated \
  --cpu=4 \
  --memory=2Gi \
  --network=default \
  --subnet=default \
  --port=8001 \
  --set-env-vars=GOOGLE_CLOUD_PROJECT=$PROJECT_ID,GOOGLE_CLOUD_LOCATION=us-central1,GOOGLE_GENAI_USE_VERTEXAI=TRUE,TOOLBOX_URL=https://springfield-toolbox-$PROJECT_NUMBER.us-central1.run.app,AGENT_URL=https://a2a-directory-agent-$PROJECT_NUMBER.us-central1.run.app/
```