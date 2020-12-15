from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Employee)
admin.site.register(Material)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Review)