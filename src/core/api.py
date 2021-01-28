from rest_framework import views, generics, status, permissions

from core.serializers import AppointmentsSerializer, BlockedDaysSerializer


class BookDoctor(views.APIView):
    """A view to let patients book a doctor"""

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: views.Request):

        data = AppointmentsSerializer(request.data)
        if data.is_valid():
            new_data = data.save()
            return views.Response(data=new_data, status=status.HTTP_201_CREATED)
        return views.Response(status=status.HTTP_400_BAD_REQUEST)


class BlockDay(generics.CreateAPIView):

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BlockedDaysSerializer
