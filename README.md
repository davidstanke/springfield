WIP demo of agents and agentic coding

## Local dev

Run the MCP server (assumes toolbox binary is already present; see README in that folder)
```
cd mcp-directory-server
./toolbox --tools-file "tools.yaml"
```

**In a new terminal**, run the agent
```
cd a2a-directory-agent
source .venv/bin/activate
uvicorn agent:a2a_app --port 8001
```

## Deploy

Deploy the MCP server
```bash
cd mcp-directory-server
export PROJECT_ID=$(gcloud config get-value project)

gcloud services enable run.googleapis.com \
   cloudbuild.googleapis.com \
   artifactregistry.googleapis.com \
   iam.googleapis.com \
   secretmanager.googleapis.com

gcloud artifacts repositories create springfield \
  --repository-format=docker \
  --location=us-central1 \
  --description="Repository for Springfield ADK agents" \
  --project=$PROJECT_ID
                       
gcloud iam service-accounts create springfield-toolbox-identity

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member serviceAccount:springfield-toolbox-identity@$PROJECT_ID.iam.gserviceaccount.com \
    --role roles/secretmanager.secretAccessor

gcloud projects add-iam-policy-binding $PROJECT_ID \
    --member serviceAccount:springfield-toolbox-identity@$PROJECT_ID.iam.gserviceaccount.com \
    --role roles/cloudsql.client

gcloud secrets create springfield-directory-tools --data-file=tools.yaml

# Deploy to Cloud Run using public base image
gcloud run deploy springfield-toolbox \
    --image us-central1-docker.pkg.dev/database-toolbox/toolbox/toolbox:latest \
    --service-account springfield-toolbox-identity \
    --region us-central1 \
    --set-secrets "/app/tools.yaml=springfield-directory-tools:latest" \
    --args="--tools-file=/app/tools.yaml","--address=0.0.0.0","--port=8080" \
    --allow-unauthenticated \
    # --set-env-vars="PROJECT_ID=$PROJECT_ID,DB_USER=postgres,DB_PASS=admin" \
```