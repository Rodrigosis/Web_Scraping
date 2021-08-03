import abc
from abc import ABC
from typing import Optional, List


class Manga:

    def __init__(self, name: str, about: Optional[str] = None, tags: Optional[List] = None,
                 last_cap: Optional[float] = None, num_cap: Optional[int] = None,
                 alternative_names: Optional[List] = None, note: Optional[float] = None,
                 status: Optional[str] = None):
        self.name = name
        self.about = about
        self.tags = tags
        self.last_cap = last_cap
        self.num_cap = num_cap
        self.alternative_names = alternative_names
        self.note = note
        self.status = status


class Scraping(ABC):

    @classmethod
    @abc.abstractmethod
    def get_data(cls, url: str):
        pass

    @classmethod
    @abc.abstractmethod
    def update(cls, name: str):
        pass
