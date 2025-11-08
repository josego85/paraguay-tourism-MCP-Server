"""Core module for configuration and dependency management."""

from .dependencies import DependencyContainer, get_container
from .imports import setup_imports

__all__ = ["DependencyContainer", "get_container", "setup_imports"]

