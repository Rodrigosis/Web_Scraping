import abc
from abc import ABC
from typing import Optional, List
from bs4 import BeautifulSoup


class Manga:

    def __init__(self, manga_id: str, name: Optional[str] = '', about: Optional[str] = '',
                 categories: Optional[List] = None, last_cap: Optional[float] = 0, last_cap_read: Optional[float] = 0,
                 num_cap: Optional[int] = 0, alternative_names: Optional[List] = None, score: Optional[float] = 0,
                 status: Optional[str] = None, author: Optional[str] = '', image: Optional[str] = None,
                 link: Optional[str] = None):
        if categories is None:
            categories = []

        if alternative_names is None:
            alternative_names = []

        if status is None:
            status = 'undefined'

        self.id = manga_id
        self.name = name
        self.about = about
        self.categories = categories
        self.last_cap = last_cap
        self.last_cap_read = last_cap_read
        self.num_cap = num_cap
        self.alternative_names = alternative_names
        self.score = score
        self.status = status
        self.author = author
        self.image = image
        self.link = link

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Categories: {self.categories}\n' \
               f'Last cap: {self.last_cap}\n' \
               f'Num caps: {self.num_cap}\n' \
               f'Score: {self.score}\n' \
               f'Status: {self.status}\n' \
               f'Author: {self.author}\n' \
               f'Alternative names: {self.alternative_names}\n' \
               f'About: {self.about}'


class Scraping(ABC):

    @classmethod
    @abc.abstractmethod
    def add_new(cls, url: str) -> Manga:
        pass

    @classmethod
    @abc.abstractmethod
    def update(cls, manga_id: str, name: str) -> Manga:
        pass

    @classmethod
    @abc.abstractmethod
    def get_html(cls, url: str) -> BeautifulSoup:
        pass

    @classmethod
    @abc.abstractmethod
    def chapters_info(cls, manga: Manga, html) -> Manga:
        pass
