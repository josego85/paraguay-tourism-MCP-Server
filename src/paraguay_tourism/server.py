"""MCP Server for Paraguay Tourism data."""

import sys
from pathlib import Path

from fastmcp import FastMCP

# Handle both relative imports (when used as module) and absolute imports (when run directly)
try:
    from .core import get_container, setup_imports
    from .handlers import register_place_handlers
except ImportError:
    # Add src directory to path when running directly
    src_path = Path(__file__).parent.parent
    if str(src_path) not in sys.path:
        sys.path.insert(0, str(src_path))
    from paraguay_tourism.core import get_container, setup_imports
    from paraguay_tourism.handlers import register_place_handlers


def create_app() -> FastMCP:
    """
    Create and configure the MCP server application.
    
    Returns:
        Configured FastMCP server instance.
    """
    # Setup imports configuration
    setup_imports()
    
    # Initialize MCP server
    mcp = FastMCP("Paraguay Tourism MCP Server 🚀")
    
    # Get dependency container
    container = get_container()
    
    # Register all handlers
    register_place_handlers(mcp, container)
    
    return mcp


# Create the app instance
mcp = create_app()


if __name__ == "__main__":
    mcp.run()
