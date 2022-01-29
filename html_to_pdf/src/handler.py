from datetime import datetime
import json

from src.utils.create_pdf import create_pdf
from src.utils.download_html import download_html
from src.utils.upload_pdf import upload_pdf


def html_to_pdf(url):
    return_msg = "not-working"
    return_flag = False
    try:
        file = create_pdf(url)
        pdf_url = upload_pdf(file)
        return_msg = pdf_url
        return_flag = True
    except Exception as err:
        print(err)

    return return_msg, return_flag


def html_to_pdf_handler(event, context):
    init_time = datetime.now()
    body = event.get("body")
    body = json.loads(body)
    url = body.get("url", None)

    if url:
        print("PROCESS INITIATED")
        return_msg, return_flag = html_to_pdf(url)
    else:
        return_msg = "No file url passed"
        return_flag = False

    current_time = datetime.now()
    tat = '{}'.format((current_time - init_time).microseconds / 1000000)

    response = {
        "statusCode": 200 if return_flag else 404,
        "headers": {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Credentials': True,
        },
        "body": json.dumps({
            "message": return_msg,
            "flag": return_flag,
            "Turn Around Time": tat
        })
    }
    return response
