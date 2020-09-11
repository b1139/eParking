from .serializers import SlotSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Slot


class ParkViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer

    @action(methods=["POST"], detail=False)
    def park(self, request):
        print(request.data)