#!/usr/bin/env python3
"""auth
Class template for all authentication system to be implemented.
"""


from flask import request
from typing import List, TypeVar
import fnmatch


class Auth():
    """Auth class to manage the API authentication."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Public method"""
        if path is None:
            return True

        if excluded_paths is None or not excluded_paths:
            return True

        for paths in excluded_paths:
            if fnmatch.fnmatch(path, paths):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Public method."""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Public method."""
        return None
