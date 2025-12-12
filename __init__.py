# pages/__init__.py
"""
Page Objects package.

Expose commonly-used page classes for easy imports:
    from pages import LoginPage, FormPage
"""

from .login_page import LoginPage
from .form_page import FormPage
from .base_page import BasePage

__all__ = [
    "BasePage",
    "LoginPage",
    "FormPage",
]
