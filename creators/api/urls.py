from django.urls import path
from creators.api.views import ContentList


urlpatterns = [
    path("content/", ContentList.as_view()),
]
