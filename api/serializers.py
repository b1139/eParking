from rest_framework import serializers
from .models import Vehicle, Slot
from .utils import get_avilable_slots


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('registration_no',)


class SlotSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(partial=True, required=False)

    class Meta:
        model = Slot
        fields = ('slot_no', 'vehicle')
        read_only_fields = ('slot_no',)
        extra_kwargs = {
            'vehicle': {'write_only': True},
        }

    def create(self, validated_data):
        vehicle_data = validated_data.pop('vehicle')
        vehicle = Vehicle.objects.create(**vehicle_data)
        slot = Slot.objects.create(parked_vehicle=vehicle, slot_no=get_avilable_slots().pop())
        return slot
