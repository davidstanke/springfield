MCP server provides directory information about the residents of Springfield. Uses the GenAI Toolbox binary to provide access to a database. Most of the interesting bits are in the `tools.yaml` file, which is mounted as a secret when run in Cloud Run (see `cloudbuild.yaml`).

Database server:
`35.223.35.223`
table: `residents`

admin user:
- `postgres` / `*64z)^8TSh]f{7@.`

read-only user:
- `springfield` / `b2zca-EoujGvjRwcg9UW`

## Running the toolbox service locally

1. Download the appropriate version of the toolbox
  ```sh
  export OS="linux/amd64" # one of linux/amd64, darwin/arm64, darwin/amd64, or windows/amd64
  curl -O https://storage.googleapis.com/genai-toolbox/v0.24.0/$OS/toolbox
  chmod +x toolbox
  ```
2. run the server
  ```sh
  ./toolbox --tools-file "tools.yaml"
  ```
  The server will be running at `0.0.0.0:5000`
  
## To deploy to Cloud Run

### Pre-req

```
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
```

### Deploy
`gcloud builds submit .`

Deployed service: `https://toolbox-617191421982.us-central1.run.app/`

## Running locally as a container
Blergh, I can't figure out how to do this. When I run it and try to curl it, I get `Recv failure: Connection reset by peer`