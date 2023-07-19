from django.contrib import admin
from django.contrib.auth.models import User,Group
from myapp.models import Dastavka
# Register your models here.



admin.site.unregister([Group])
admin.site.register(Dastavka)