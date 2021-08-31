import os
import pathlib
from dotenv import load_dotenv
import boto3

load_dotenv()
s3_bucket = os.getenv('AWS_S3_BUCKET')

aws_access_key = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region = os.getenv('AWS_REGION_NAME')


class Storage:

    def __init__(self):
        self.s3 = boto3.resource('s3')
        self.image_path = str(pathlib.Path(__file__).parent.resolve()) + '/images/'

    def set_file(self, image_name: str, folder: str):
        s3_object = self.s3.Object(s3_bucket, folder + image_name)
        s3_object.put(Body=self.image_path + image_name)
        os.remove(self.image_path + image_name)

    def get_file(self):
        pass

    def local_set_file(self, image_name: str, folder: str):
        """
        This method don't work yet
        """
        session = boto3.Session(
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
            region_name=aws_region
        )
        s3 = session.resource('s3')
        s3_object = s3.Object(s3_bucket, folder + image_name)
        with open(self.image_path + image_name, "rb") as img:
            s3_object.put(Body=img)
