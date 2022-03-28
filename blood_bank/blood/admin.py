from django.contrib import admin
from blood.models import District, Branch, BloodGroup, Donor

# Register your models here.

admin.site.register(District)
admin.site.register(Branch)
admin.site.register(BloodGroup)
admin.site.register(Donor)
