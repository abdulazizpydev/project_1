from storages.backends.s3boto3 import S3Boto3Storage

class StaticRoot3Boto3Storage(S3Boto3Storage):
    location = 'static'


class MediaRoot3Boto3Storage(S3Boto3Storage):
    location = 'media'

