def paginate_list(items: list, page: int, size: int):
    """
    Paginate list

    Args:
        items (list): The list of items
        page (int): The page
        size (int): The size

    Returns:
        list
    """
    # Calculate start and end indices
    start = (page - 1) * size
    end = start + size

    # Return the sliced list
    return items[start:end] if start < len(items) else []
