import pdfkit


def create_pdf(url):
    print("Create PDF")
    config = pdfkit.configuration(wkhtmltopdf="/opt/bin/wkhtmltopdf")
    options = {
        'javascript-delay': '25000',
        'disable-smart-shrinking': '',
    }
    pdf = pdfkit.from_url(url, False, configuration=config, options=options)
    print("Return PDF")
    return pdf
