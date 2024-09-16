from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException, status

from app.core.settings import get_settings

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

    async def verify(self, token: str, sub_head: str, _: bool = True):
        """This method verifies the token.

        Args:
            token (str): The refresh token.
            sub_head (str): The sub head of the token
            raise_exception (bool = True): raise an exception if token is invalid

        Returns:
            str | None: The sub's ID.
        """
        try:
            payload = jwt.decode(
                jwt=token,
                key=self.secret_key,
                algorithms=["HS256"],
            )
            sub: str = payload.get("sub")

            if payload.get("type") != "access":
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token"
                )

            if sub.split("-")[0] != sub_head:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token"
                )
            return "".join(sub.split("-")[1:])

        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Access Token Has Expired",
            )

        except jwt.PyJWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Token"
            )
