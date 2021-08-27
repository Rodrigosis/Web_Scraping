import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    AWS_S3_BUCKET: str = os.getenv('AWS_S3_BUCKET')


settings = Settings()
