from rest_framework import (status, viewsets)
from rest_framework.response import Response
from rest_framework.decorators import list_route
from .tasks import download_url_as_html
# Create your views here.


class URLDownloader(viewsets.ViewSet):
    """
    To create router for accepting post requests.
    """

    @list_route(url_path="download_urls", methods=['post', ])
    def download_urls_and_email_zip(self, request):
        """ accept request parameters and pass to backgound tasks. """
        if request.data.get('urls') and request.data.get('emails'):
            download_url_as_html.delay(request.data.get(
                'urls'), request.data.get('emails'))
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"details": "urls and emails fields are compulsory fields"})
        return Response(status=status.HTTP_200_OK, data={"details": "urls and emails handover successfully to background tasks for further processing"})
