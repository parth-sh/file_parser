import requests
from datetime import datetime
import boto3


def upload_to_s3(file,bucket_name,key,content_type,content_encoding):
    '''Takes a pdf file blob and uploads to s3 storage.'''
    file.seek(0)
    try:
        init_time = datetime.now()
        print("Initiating s3 upload")
        
        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)

        bucket.put_object(Key=key, Body=file.read(), ACL='public-read',ContentType=content_type,ContentEncoding=content_encoding)
        current_time = datetime.now()
        print("pdf uploaded in {} seconds".format((current_time - init_time).microseconds / 1000000))
        return f'https://{bucket_name}.s3.amazonaws.com/{key}' 
             
    except Exception as err:
        print(err,'\n s3 bucket initiation problem \n')
        return None


def download_from_url(file_url):
    '''Downloads encrypted file from url.'''
    print("Initiating file download file URL={}".format(file_url))
    try:
        response = requests.get(file_url)
        print("Download complete")
        return response.content, response.headers['Content-Type']
    except Exception as err:
        print(err,'\n Encrypted file download problem \n')
        return None, None
