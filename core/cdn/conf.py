import os


AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY_ID = os.environ.get('AWS_SECRET_ACCESS_KEY_ID')
AWS_S3_SIGNATURE_VIRSION = 's3v4'
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_ENDPOINT_URL = 'https://fra1.digitaloceanspaces.com'
AWS_ENDPOINT = 'fra1.digitaloceanspaces.com'
AWS_S3_OBJECT_PARAMETRS = {
    "CacheControl": "max-age=86400",
}

DEFAULT_FILE_STORAGE = 'core.cdn.backends.MediaRoot3Boto3Storage'
STATICFILES_STORAGE = 'core.cdn.backends.StaticRoot3Boto3Storage'




