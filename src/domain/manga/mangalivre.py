from src.domain.scraping import Scraping, Manga


class MangaLivre(Scraping):

    def __init__(self):
        pass

    def get_data(self, url: str) -> Manga:
        pass

    def update(self, name: str) -> Manga:
        pass
