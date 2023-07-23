#!/usr/bin/env python3
"""
Takes two integer args with default values.
"""
import csv
import math
from typing import List, Dict
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

    def get_hyper(self, page: int = 1, pg_z: int = 10) -> Dict:
        """
        Implementation.
        """
        hyper_dict = dict()
        pages = int(len(self.dataset()))
        hyper_dict["page_size"] = len(self.get_page(page, pg_z))
        hyper_dict["page"] = page
        hyper_dict["data"] = self.get_page(page, pg_z)
        hyper_dict["next_page"] = page + 1 if page <= (pages/pg_z) else None
        hyper_dict["prev_page"] = page - 1 if page != 1 else None
        hyper_dict["total_pages"] = int(len(self.dataset())/pg_z)
        return hyper_dict
