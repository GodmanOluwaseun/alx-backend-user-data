#!/usr/bin/env python3
"""Basic authentication.
"""

from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Class that inherits from Auth class"""
    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """
        Returns the Base64 part of the
        Authorization header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        else:
            encoded_str = authorization_header.split(' ', 1)[1]
            return encoded_str

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Returns the decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except(TypeError, UnicodeDecodeError):
            return None
