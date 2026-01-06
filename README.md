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
uvicorn agent:a2a_app
```

## Deploy
(see subfolders)
