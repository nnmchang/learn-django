from django.urls import path

from app.views import SampleApi

urlpatterns = [
    path("sample", SampleApi.as_view(), name="sample"),
]
