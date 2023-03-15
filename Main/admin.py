from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Employee)
admin.site.register(models.Assets)
admin.site.register(models.Delegation)