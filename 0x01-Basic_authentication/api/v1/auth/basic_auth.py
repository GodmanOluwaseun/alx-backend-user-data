#!/usr/bin/env python3
"""Basic authentication.
"""

from api.v1.auth.auth import Auth
import base64
from typing import Tuple, TypeVar
from models.user import User


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
            decoded = base64.b64decode(
                base64_authorization_header, validate=True
            )
            return decoded.decode('utf-8')
        except(TypeError, UnicodeDecodeError, base64.binascii.Error):
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> Tuple[str, str]:
        """
        Returns the user email and password from
        the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)

        user_details = decoded_base64_authorization_header.split(':', 1)
        return (user_details[0],  user_details[1])

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """Returns user instance based on the credentials given"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_email, str):
            return None

        try:
            users = User.search({'email': user_email})
        except (Exception):
            return None

        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Overloads Auth and retrieves the User instance for a request
        """
        try:
            header = self.authorization_header(request)
            encoded = self.extract_base64_authorization_header(header)
            decoded_header = self.decode_base64_authorization_header(encoded)
            user_d = self.extract_user_credentials(decoded_header)
            return self.user_object_from_credentials(user_d[0], user_d[1])
        except (Exception):
            return None
