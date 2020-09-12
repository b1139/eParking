from decouple import config
from pytimeparse.timeparse import timeparse
from rest_framework import throttling

from api.models import Slot


def is_full():
    """
    Checks whether the slot is full or not
    :return: True/False
    """
    # Retrieves the maximum slots from the Config, converst to int
    maximum_slot = config('SLOT_SIZE', cast=int)
    # Retrieves list of slots where vehicle is parked
    total_occupied_slots = Slot.objects.exclude(parked_vehicle__isnull=True).count()
    return True if maximum_slot == total_occupied_slots else False


def get_avilable_slots():
    """
    To identify the list of slots available
    :return: List of available slots
    """
    # All available slots , if SLOT SIZE = 2 then  all_slots={1,2}
    all_slots = set(_ for _ in range(1, config('SLOT_SIZE', cast=int) + 1))
    # Slots where vehicle already parked assume booked_slots = {1}
    booked_slots = set(Slot.objects.filter(parked_vehicle__isnull=False).values_list('slot_no', flat=True))
    # Subtraction of two sets will result in available slots {1, 2}-{1} = {1}
    available_slots = all_slots - booked_slots
    return available_slots


class EParkingThrottle(throttling.AnonRateThrottle):
    def parse_rate(self, rate):
        """
        Given the request rate string, return a two tuple of:
        <allowed number of requests>, <period of time in seconds>
        """
        if rate is None:
            return (None, None)
        num, period = rate.split('/')
        num_requests = int(num)
        duration = timeparse(period)
        return num_requests, duration
