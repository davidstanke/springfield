MCP server provides directory information about the residents of Springfield.

To run the server:
1. Download the appropriate version of the toolbox
  ```sh
  export OS="linux/amd64" # one of linux/amd64, darwin/arm64, darwin/amd64, or windows/amd64
  curl -O https://storage.googleapis.com/genai-toolbox/v0.22.0/$OS/toolbox
  chmod +x toolbox
  ```
2. run the server
  ```sh
  ./toolbox --tools-file "tools.yaml"
  ```