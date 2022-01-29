import json
from src.utils.constants import imgpath,pdfpath
from src.utils.file_transformers import decrypt_pdf_blob,pdf_to_img_save
from src.utils.file_transfers import upload_to_s3,download_from_url
from src.utils.constants import bucket_name,pdfkey,imgkey,pdf_content_type,pdf_content_encoding,image_content_encoding,image_content_type


def decrypt_pdf(file_url,password,file_format):
    return_msg = None
    return_flag = False
    return_service = None

    file_blob, content_type = download_from_url(file_url)
    if content_type != 'application/pdf':
        return_msg = 'Wrong File format. Please upload a PDF file.'
        return return_msg, return_flag, return_service

    pdf_file = decrypt_pdf_blob(file_blob,password)
    
    if(file_format=='image'):
        img_file = pdf_to_img_save(pdf_file)
        return_msg = upload_to_s3(img_file,bucket_name,imgkey,pdf_content_type,pdf_content_encoding)

    if(file_format=='pdf' or file_format==None):
        return_msg = upload_to_s3(pdf_file,bucket_name,pdfkey,pdf_content_type,pdf_content_encoding)

    if return_msg!=None:
        return_flag = True
        return_service = 'DECRYPTION LIBRARY'

    pdf_file.close()
    return return_msg, return_flag, return_service


def handler(event, context):
    '''Lambda handler function'''

    body = event.get("body")
    body = json.loads(body)
    file_url = body.get("file_url", None)
    password = body.get("password", None)
    file_format = body.get("format", None)

    if file_url :
        print('''Decrypting password protected PDF file. 
        \nfile_URL={} \npassword={} \nfile_format={}'''.format(file_url,password,file_format))
        return_msg, return_flag, return_service = decrypt_pdf(file_url,password,file_format)
    else:
        return_msg = "No file passed"
        return_flag = False
        return_service = None

    body = {
        "message": return_msg,
        "flag": return_flag,
        "service_used": return_service
    }

    response = {
        "statusCode": 200 if return_flag else 404,
        "body": json.dumps(body)
    }
    return response