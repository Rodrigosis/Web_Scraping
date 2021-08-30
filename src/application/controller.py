from fastapi import APIRouter, Depends

from src.logging_config import logger
from src.application.validation.validation import Pages, validate
from src.application.res_req import ObjRequest, ObjResponse, MangaPutRequest, MangaPutResponse
from src.domain.manga.url_one import UrlOne

router = APIRouter()
# get -> get all mangas
# post -> get specifics mangas
# put -> put mangas
# delete -> delete mangas


@router.get("/manga", response_model=ObjResponse)
async def manga():

    log_info = f'foobar log'
    logger.info(log_info)

    return ObjResponse(data={'foo': 'bar'})


@router.post("/manga", response_model=ObjResponse)
async def manga(data: ObjRequest = Depends()):

    log_info = f'foobar log {data.name}'
    logger.info(log_info)

    return ObjResponse(data={'foobar': data.name})


@router.put("/manga", response_model=MangaPutResponse)
async def manga(data: MangaPutRequest = Depends()):
    mangas = []

    for link in data.links:
        v = validate(link)
        if v == Pages.URL_ONE:
            new_manga = UrlOne().add_new(link)
            mangas.append(new_manga.to_json())
        else:
            raise Exception("Not found scraping script for this page.")

    log_info = f'foobar log'
    logger.info(log_info)

    return MangaPutResponse(data=mangas)


@router.delete("/manga", response_model=ObjResponse)
async def manga(data: ObjRequest = Depends()):

    log_info = f'foobar log {data.name}'
    logger.info(log_info)

    return ObjResponse(data={'foobar': data.name})


@router.post("/doujinshi", response_model=ObjResponse)
async def doujinshi(data: ObjRequest = Depends()):

    log_info = f'foobar log {data.name}'
    logger.info(log_info)

    return ObjRequest()


@router.post("/anime", response_model=ObjResponse)
async def anime(data: ObjRequest = Depends()):

    log_info = f'foobar log {data.name}'
    logger.info(log_info)

    return ObjRequest()


@router.post("/movie", response_model=ObjResponse)
async def movie(data: ObjRequest = Depends()):

    log_info = f'foobar log {data.name}'
    logger.info(log_info)

    return ObjRequest()
