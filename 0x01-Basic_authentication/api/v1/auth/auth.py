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

        normal_path = path.rstrip('/')

        for paths in excluded_paths:
            if fnmatch.fnmatch(normal_path, paths.rstrip('/')):
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """Public method."""
        if request is None:
            return None

        if request.get('Authorization') is None:
            return None

        return request.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """Public method."""
        return None
