#!/usr/bin/env python3
"""
Takes two integer args with default values.
"""
import csv
import math
from typing import List
index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Implementation.
        """
        assert (type(page) == int and type(page_size) == int
               and page_size and page > 0)
        try:
            indices = index_range(page, page_size)
            return self.dataset()[indices[0]: indices[1]]
        except Exception as error:
            return list()
