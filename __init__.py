# utils/__init__.py
"""
Utilities package (helpers used across tests).

Expose helper functions so you can import like:
    from utils import save_screenshot
"""
from .screenshot_helper import save_screenshot

__all__ = [
    "save_screenshot",
]
