from fastapi import APIRouter
from typing import List, Dict

# from src.logging_config import logger
from src.application.validation.validation import Pages, validate
from src.domain.manga.url_one import UrlOne
from src.infra.database import Database

router = APIRouter()


@router.get("/manga")
async def get_all_mangas() -> List[Dict]:
    data = Database().get_manga()

    mangas = []
    for i in data:
        mangas.append(i.to_json())

    return mangas


@router.post("/manga")
async def get_mangas(ids: List[str]) -> List[Dict]:
    data = Database().get_manga(ids)

    mangas = []
    for i in data:
        mangas.append(i.to_json())

    return mangas


@router.post("/manga/add")
async def add_mangas(data: List[str]) -> List[Dict]:

    mangas = []

    for link in data:
        v = validate(link)
        if v == Pages.URL_ONE:
            new_manga = UrlOne().add_new(link)
            mangas.append(new_manga.to_json())
        else:
            raise Exception("Not found scraping script for this page.")

    return mangas


@router.post("/manga/remove")
async def remove_mangas(data: List[str]) -> Dict:

    return {'foobar': 'foo'}


@router.post("/doujinshi")
async def doujinshi(data: List[str]) -> Dict:

    return {}


@router.post("/anime")
async def anime(data: List[str]) -> Dict:

    return {}


@router.post("/movie")
async def movie(data: List[str]) -> Dict:

    return {}
