"""Module for handling import configuration."""

import sys
from pathlib import Path


def setup_imports() -> None:
    """
    Configure imports to handle both relative (module) and absolute (direct execution) imports.
    
    This ensures the package works both when imported as a module and when run directly.
    """
    try:
        # Try relative imports first (when used as module)
        from ..repositories import PlaceRepository  # noqa: F401
        from ..services import PlaceFormatter  # noqa: F401
    except ImportError:
        # Add src directory to path when running directly
        src_path = Path(__file__).parent.parent.parent
        if str(src_path) not in sys.path:
            sys.path.insert(0, str(src_path))

