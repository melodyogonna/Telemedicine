from os import name
from django.urls import path

from core.api import BookDoctor


generic_views = [path("bookdocktor", BookDoctor.as_view(), name="api-book-doctor")]

urlpatterns = generic_views
