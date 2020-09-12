from rest_framework import serializers
from .models import Vehicle, Slot
from .utils import get_avilable_slots, is_full


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('registration_no',)


class ParkInfoSerializer(serializers.ModelSerializer):
    parked_vehicle = serializers.SlugRelatedField(slug_field="registration_no", queryset=Vehicle.objects.all())

    class Meta:
        model = Slot
        fields = ('slot_no', 'parked_vehicle')


class SlotSerializer(serializers.ModelSerializer):
    vehicle = VehicleSerializer(partial=True, required=False)

    class Meta:
        model = Slot
        fields = ('slot_no', 'vehicle')
        read_only_fields = ('slot_no',)
        extra_kwargs = {
            'vehicle': {'write_only': True},
        }

    def validate(self, attrs):
        # Checks Whether the slots are full before parking the vehicle
        if is_full():
            raise serializers.ValidationError({"message": "No More Slots Available For Parking!!!"})
        return attrs

    def create(self, validated_data):
        vehicle_data = validated_data.pop('vehicle')
        vehicle = Vehicle.objects.create(**vehicle_data)
        # Getting Available slots which does not have vehicle parked
        # And links the available slots to newly parked vehicle
        slot, _ = Slot.objects.get_or_create(slot_no=get_avilable_slots().pop())
        slot.parked_vehicle = vehicle
        slot.save()
        return slot
