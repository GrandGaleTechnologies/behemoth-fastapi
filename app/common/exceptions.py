class NotFound(Exception):
    """
    Common base class for all 404 responses
    """

    def __init__(self, *, msg: str, loc: list = []):
        self.msg = msg
        self.loc = loc
