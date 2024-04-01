from storages.backends.s3boto import S3BotoStorage

class StaticRoot3Boto3Storage(S3BotoStorage):
    location = 'static'


class MediaRoot3Boto3Storage(S3BotoStorage):
    location = 'media'

