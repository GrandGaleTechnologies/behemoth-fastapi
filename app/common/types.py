"""This module contains common types used in the application."""

from typing import Literal, NamedTuple


class PaginationParamsType(NamedTuple):
    """The pagination parameters for the application."""

    q: str | None
    page: int
    size: int
    order_by: Literal["asc", "desc"]
