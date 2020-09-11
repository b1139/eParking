from django.contrib import admin

# Register your models here.
from api.models import Vehicle, Slot

admin.site.register([Vehicle, Slot])