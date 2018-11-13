import os
import urllib3
import zipfile
import tempfile
from celery import task
from django.conf import settings
from django.template import Context
from django.core.mail import EmailMessage
from django.template.loader import get_template


@task
def email_zip(emails, errors, zipfile):
    """
    Accepts emails, error log dict and zipfile path and send an
    emails to provided emails with zip as an attachment.
    """
    recipient = []
    for email in emails.split(','):
        recipient.append(email)
    msg = EmailMessage(
        'Html Files Zip - Assignment', 'ErrorLog: \n' + str(errors), settings.EMAIL_HOST_USER, to=[] + recipient
    )
    msg.attach_file(zipfile, mimetype='application/octet-stream')
    msg.send()
    os.remove(zipfile)


@task
def download_url_as_html(urls, emails):
    """
    Accepts urls and emails lists and download html from provided urls
    and create zip file of html files.
    """
    errors = {}
    with tempfile.NamedTemporaryFile(suffix='_%s' % 'urls_html.zip', delete=False) as tmp:
        with zipfile.ZipFile(tmp.name, 'w') as htmlzip:
            for url in urls.split(','):
                try:
                    conn = urllib3.connection_from_url(url)
                    content = conn.request('GET', '/', assert_same_host=False)
                except Exception as e:
                    errors.update({url: str(e.reason)})
                    continue
                domain = url.split('//')
                fp = tempfile.NamedTemporaryFile(
                    prefix='%s_' % domain[1] if domain[1] else domain[0])
                fp.write(content._body)
                htmlzip.write(fp.name)
                fp.close()
        email_zip.delay(emails, errors, tmp.name)
    return {}
