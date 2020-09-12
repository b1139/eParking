from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework import viewsets, generics
from rest_framework.response import Response

from .models import Slot
from .serializers import SlotSerializer, ParkInfoSerializer


class ParkViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    """
    Park management class
    1. Parks a Vehicle
    2. Unparks a Vehicle
    """

    queryset = Slot.objects.all()
    serializer_class = SlotSerializer
    lookup_field = "slot_no"

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        msg = f"Slot {instance.slot_no} has no car parked"
        if instance.parked_vehicle:
            instance.parked_vehicle.delete()
            msg = f"Slot {instance.slot_no} is available for parking now"
        return Response({"message": msg})


class ParkInfoViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    """
    1. Lists the list of slots available
    2. List by the slot_no
    3. List by parked_vehicle__registration_no (vehicle registration no)
    """
    queryset = Slot.objects.all()
    serializer_class = ParkInfoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['slot_no', 'parked_vehicle__registration_no']
