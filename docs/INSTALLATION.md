# 📦 Installation Guide

## Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/paraguay-tourism-MCP-Server.git
cd paraguay-tourism-MCP-Server
```

### 2. Create Virtual Environment

```bash
python3.11 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Running the Server

```bash
python src/paraguay_tourism/server.py
```

## Configuring Cursor Desktop

Add the following configuration to your `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "paraguay-tourism-mcp-server": {
      "command": "/path/to/venv/bin/python",
      "args": [
        "/path/to/src/paraguay_tourism/server.py"
      ]
    }
  }
}
```

**Note**: Replace `/path/to/` with the actual path to your project directory.

### Example Configuration

```json
{
  "mcpServers": {
    "paraguay-tourism-mcp-server": {
      "command": "/home/user/paraguay-tourism-MCP-Server/venv/bin/python",
      "args": [
        "/home/user/paraguay-tourism-MCP-Server/src/paraguay_tourism/server.py"
      ]
    }
  }
}
```

## Verification

After installation, verify that the server runs correctly:

```bash
python src/paraguay_tourism/server.py
```

You should see the MCP server starting without errors.

## Troubleshooting

### Python Version Issues

Ensure you're using Python 3.11 or higher:

```bash
python --version  # Should show 3.11+
```

### Virtual Environment Issues

If you encounter import errors, make sure the virtual environment is activated:

```bash
which python  # Should point to venv/bin/python
```

### Missing Dependencies

If you see import errors, reinstall dependencies:

```bash
pip install -r requirements.txt --force-reinstall
```

