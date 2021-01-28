from os import name
from django.urls import path

from core.api import BookDoctor, BlockDay


generic_views = [
    path("bookdocktor/", BookDoctor.as_view(), name="api-book-doctor"),
    path("block-day/", BlockDay.as_view(), name="api-block-day"),
]

urlpatterns = generic_views
