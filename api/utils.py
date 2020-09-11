from decouple import config

from api.models import Slot


def is_full():
    """
    Checks whether the slot is full or not
    :return: True/False
    """
    maximum_slot = config('SLOT_SIZE', cast=int)
    total_occupied_slots = Slot.objects.exclude(parked_vehicle__isnull=True).count()
    return True if maximum_slot == total_occupied_slots else False


def get_avilable_slots():
    """
    To identify the list of slots available
    :return: Tuple(List of available slots, slot to be crated)
    """
    all_slots = set(_ for _ in range(1, config('SLOT_SIZE', cast=int) + 1))
    booked_slots = set(Slot.objects.filter(parked_vehicle__isnull=False).values_list('slot_no', flat=True))
    print(all_slots, booked_slots)
    available_slots = all_slots - booked_slots
    return available_slots
