from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from sqlalchemy import Column

# Globals
ph = PasswordHasher()


async def hash_password(*, raw: str):
    """
    Hash password
    """
    return ph.hash(raw)


async def verify_password(*, raw: str, hashed: str | Column[str]):
    """
    Verify password
    """
    try:
        return ph.verify(hash=str(hashed), password=raw)
    except VerifyMismatchError:
        return False
