from django.contrib import admin
from .models import Project
from .models import ContactMessage

admin.site.register(ContactMessage)
admin.site.register(Project)

# Register your models here.
