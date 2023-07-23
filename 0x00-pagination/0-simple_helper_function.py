#!/usr/bin/env python3
"""
Function that takes two integer arguments page and page_size.
"""
from typing import Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    """
    Returns a tuple of size two containing start and end index.
    """
    return ((page_size * page) - page_size, page_size * page)
