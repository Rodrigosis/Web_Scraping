import os
from dotenv import load_dotenv
from pymongo import MongoClient
from typing import List, Optional

from src.domain.scraping import Manga

load_dotenv()
db_uri = os.getenv('DB_URI')


class Database:

    def __init__(self):
        self.db = MongoClient(db_uri)

    def set_manga(self, manga: Manga):
        data = {'id': manga.id,
                'name': manga.name,
                'about': manga.about,
                'categories': manga.categories,
                'last_cap': manga.last_cap,
                'last_cap_read': manga.last_cap_read,
                'num_cap': manga.num_cap,
                'alternative_names': manga.alternative_names,
                'score': manga.score,
                'status': manga.status,
                'author': manga.author,
                'image': manga.image,
                'link': manga.link}

        self.db.manga.mangas.insert_one(data)

    def get_manga(self, manga_ids: Optional[List[str]] = None) -> List[Manga]:
        if manga_ids is None:
            data = list(self.db.manga.mangas.find({}))
        else:
            data = []
            for i in manga_ids:
                results = list(self.db.manga.mangas.find({'id': i}))
                data.extend(results)

        mangas = [
            Manga(manga_id=manga['id'],
                  name=manga['name'],
                  author=manga['author'],
                  categories=list(manga['categories']),
                  last_cap=float(manga['last_cap']),
                  last_cap_read=float(manga['last_cap_read']),
                  num_cap=int(manga['num_cap']),
                  alternative_names=list(manga['alternative_names']),
                  score=float(manga['score']),
                  status=manga['status'],
                  about=manga['about'],
                  image=manga['image'],
                  link=manga['link'])
            for manga in data]

        return mangas
