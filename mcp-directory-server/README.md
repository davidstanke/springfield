MCP server provides directory information about the residents of Springfield. Uses the GenAI Toolbox binary to provide access to a database. Most of the interesting bits are in the `tools.yaml` file, which is mounted as a secret when run in Cloud Run (see `cloudbuild.yaml`).

Database server:
`35.223.35.223`
table: `residents`

admin user:
- `postgres` / `*64z)^8TSh]f{7@.`

read-only user:
- `springfield` / `b2zca-EoujGvjRwcg9UW`

To run the server:
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
  
Deployed to cloud: `https://toolbox-617191421982.us-central1.run.app/`
