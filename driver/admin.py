from django.contrib import admin
from driver import models


admin.site.register(models.Driver)
admin.site.register(models.Taxi)