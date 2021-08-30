import os
import pathlib
from dotenv import load_dotenv
import boto3

load_dotenv()
s3_bucket = os.getenv('AWS_S3_BUCKET')
s3_folder = os.getenv('AWS_S3_FOLDER_BINANCE_PRICES')

aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_REGION_NAME')


class Storage:

    def __init__(self):
        self.s3 = boto3.resource('s3')
        self.image_path = str(pathlib.Path(__file__).parent.resolve()) + '/images/'

    def set_file(self, image_name: str):
        s3_object = self.s3.Object(s3_bucket, s3_folder + f'mangas/covers/{image_name}')
        s3_object.put(Body=self.image_path + image_name)
        os.remove(self.image_path + image_name)

    def get_file(self):
        pass
