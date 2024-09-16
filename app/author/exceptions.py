from app.common.exceptions import NotFound


class AuthorNotFound(NotFound):
    """
    Exception for 404 Author Not Found
    """

    def __init__(self, *, loc: list | None = None):
        super().__init__("Author not found", loc=loc)
