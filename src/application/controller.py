from fastapi import APIRouter, Depends

from src.logging_config import logger
from src.application.res_req import ObjRequest, ObjResponse
from src.domain.manga.brmangas import BrMangas

router = APIRouter()
# get -> get all mangas
# post -> get specifics mangas
# put -> put mangas
# delete -> delete mangas


@router.post("/manga", response_model=ObjResponse)
async def manga(data: ObjRequest = Depends()):

    log_info = f'foobar log {data.name}'
    logger.info(log_info)

    # BrMangas().add_new()

    return ObjRequest()


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
