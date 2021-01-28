from django.http import HttpRequest, HttpResponse
from rest_framework import views
from rest_framework import request

from core.serializers import AppointmentsSerializer


class BookDoctor(views.APIView):
    """A view to let patients book a doctor"""

    def post(self, request: views.Request):
        

        data = AppointmentsSerializer(request.data)
        data.save()
        print(data)
        return views.Response(data.data)
