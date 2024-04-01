from storages.backends.s3boto3 import S3BotoStorage


class StaticRoot3Boto3Storage(S3BotoStorage):
    location = 'static'


class MediaRoot3Boto3Storage(S3BotoStorage):
    location = 'media'

