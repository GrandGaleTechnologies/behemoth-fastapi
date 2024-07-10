from app.core.database import SessionLocal


def get_session():
    """This function creates a db session"""
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
