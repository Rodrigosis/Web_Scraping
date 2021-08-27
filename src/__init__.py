from fastapi import FastAPI
from src.logging_config import logger
from src.application import controller


app = FastAPI()
app.include_router(controller.router, prefix='/scraping', tags=['scraping_route'])
logger.info('---------------- Started FastAPI ----------------')
