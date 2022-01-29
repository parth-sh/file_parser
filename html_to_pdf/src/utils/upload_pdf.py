import boto3 as boto3

from src.utils.constants import s3BucketName, objectName


def upload_pdf(file):
    print("Upload PDF")
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(s3BucketName)
    bucket.put_object(Key=objectName, Body=file, ACL='public-read', ContentType='application/pdf',
                      ContentEncoding='ascii')
    print("Return URL")
    return 'https://{}.s3.amazonaws.com/{}'.format(s3BucketName, objectName)
