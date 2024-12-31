from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException, status

from app.common.exceptions import Unauthorized
from app.core.settings import get_settings

# Globals
settings = get_settings()


class TokenGenerator:
    """
    This class is used to generate and verify JWT tokens.
    """

    def __init__(self, *, secret_key: str, expire_in: int):
        self.secret_key = secret_key
        self.expire_in = expire_in

    async def generate(self, sub: str):
        """This method generates a JWT token.

        Args:
            sub (str): The subject of the token, typically the user's ID.

        Returns:
            str: The generated token.
        """

        # Check if sub is valid
        if "-" not in sub:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Internal Server Error: Invalid Token sub",
            )

        iat = datetime.now()
        expire = iat + timedelta(minutes=self.expire_in)

        data = {
            "type": "access",
            "sub": sub,
            "iat": iat.timestamp(),
            "exp": expire.timestamp(),
            "iss": "dsspoi.confidential",
        }
        return jwt.encode(
            data,
            key=self.secret_key,
            algorithm="HS256",
        )

    async def verify(self, token: str, sub_head: str) -> str | None:
        """
        Verifies the provided JWT token.

        Args:
            token (str): The JWT token to verify.
            sub_head (str): Expected prefix of the 'sub' field in the token payload.

        Returns:
            str | None: The sub's ID if verification succeeds, or None if invalid.

        Raises:
            Unauthorized: If the token is invalid or expired.
        """
        try:
            # Decode and validate the token
            payload = jwt.decode(
                jwt=token,
                key=self.secret_key,
                algorithms=["HS256"],
            )

            # Extract and validate the 'sub' field
            sub: str | None = payload.get("sub")
            if not sub:
                raise Unauthorized("Token is missing the 'sub' field")

            # Ensure the token is of type 'access'
            if payload.get("type") != "access":
                raise Unauthorized("Token type is invalid")

            # Validate the 'sub' structure
            sub_parts = sub.split("-")
            if sub_parts[0] != sub_head or len(sub_parts) < 2:
                raise Unauthorized("Token 'sub' field structure is invalid")

            # Return the ID part of 'sub'
            return "".join(sub_parts[1:])

        except jwt.ExpiredSignatureError:
            raise Unauthorized("Token has expired")

        except jwt.PyJWTError:
            raise Unauthorized("Token verification failed")
