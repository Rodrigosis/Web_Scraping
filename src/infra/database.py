import os
from dotenv import load_dotenv
from pymongo import MongoClient

from src.domain.scraping import Manga

load_dotenv()
db_uri = os.getenv('MONGO_DB_URI')


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

        self.db.main.mangas.insert_one(data)

    def get_manga(self, manga_id: str) -> Manga:
        data = list(self.db.main.mangas.find({'id': manga_id}))[0]

        return Manga(manga_id=data['id'],
                     name=data['name'],
                     author=data['author'],
                     categories=list(data['categories']),
                     last_cap=float(data['last_cap']),
                     last_cap_read=float(data['last_cap_read']),
                     num_cap=int(data['num_cap']),
                     alternative_names=list(data['alternative_names']),
                     score=float(data['score']),
                     status=data['status'],
                     about=data['about'],
                     image=data['image'],
                     link=data['link'])
