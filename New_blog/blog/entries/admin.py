from django.contrib import admin
from .models import Entry

# Registers blog app the django admin backend.
admin.site.register(Entry)
