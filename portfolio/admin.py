from django.contrib import admin

# Register your models here. Quale modello far vedere nella schermata admin

from .models import Project

admin.site.register(Project)
