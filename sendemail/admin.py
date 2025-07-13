from django.contrib import admin
from .models import Mails, Topic

# Register your models here.
admin.site.register(Topic)
admin.site.register(Mails)