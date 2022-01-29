from io import BytesIO
from PyPDF2 import PdfFileReader, PdfFileWriter
from pdf2image import convert_from_path,convert_from_bytes
from src.utils.constants import imgpath,pdfpath,poppler_path


def decrypt_pdf_blob(file_blob,password):
    '''Decrypt file blob if password protected else returns
        using /tmp directory storage 512 MB to store assets'''
    print("Initiating file decryption \npassword={}".format(password))
    output_file = open(pdfpath, 'wb+')
    try:
        reader = PdfFileReader(BytesIO(file_blob))
        
        if(reader.isEncrypted and password!=None):
            reader.decrypt(password)
            print('File Decrypted')
            writer = PdfFileWriter()
            for i in range(reader.getNumPages()):
                writer.addPage(reader.getPage(i))
            writer.write(output_file)
        else:
            print('File already Decrypted')
            return file_blob
            
        return output_file
    except Exception as err:
        print(err,'\n decrypt library problem \n')
        return None



def pdf_to_img_save(pdf_file):
    '''Returns Image File'''
    print("Initiating pdf to image conversion")
    pdf_file.seek(0)
    img_file = open(imgpath, 'wb+')
    pages = convert_from_bytes(pdf_file.read(), 500, poppler_path=poppler_path)
    for page in pages:
        page.save(img_file, 'JPEG')
        print("Pdf converted to Image Saved")
    return img_file