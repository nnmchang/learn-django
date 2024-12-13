from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView, status


# Create your views here.
class SampleApi(APIView):
    def get(self, _res):
        return Response("OK", status=status.HTTP_200_OK)

class IndexView(TemplateView):
    template_name = "index.html"
