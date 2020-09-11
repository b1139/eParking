from rest_framework import serializers
from .models import Vehicle, Slot


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('registration_no',)


class SlotSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer()

    class Meta:
        model = Slot
        fields = ('slot_no', 'vehicle')
        read_only_fields = ('slot_no',)
        extra_kwargs = {
            'vehicle': {'write_only': True},
        }