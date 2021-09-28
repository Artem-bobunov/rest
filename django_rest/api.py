from rest_fraemwork import views, permissions
from .models import meterReadings
from .serializers import restSerializer


class restViewSet(viewsets.ModelViewSet):
    queryset = meterReadings.objects.all()
    permission_classes = [
        permissions.AllwAny
    ]
    serializer_class = restSerializer
