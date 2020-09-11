from decouple import config
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Slot
from .serializers import SlotSerializer
from .utils import is_full


class ParkViewSet(viewsets.ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer

    @action(methods=["POST"], detail=False)
    def park(self, request):
        """
        Parks a vehicle - car/bike/cycle/scooter
        :param request:
        :return: Slot No Assigned for requested Vehicle
        """
        # check whether all slot are full or not
        if is_full():
            return Response({"message": "No More Slots Available For Parking!!!"})
        else:
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
