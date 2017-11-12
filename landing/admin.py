from django.contrib import admin
from .models import Character
# Register your models here.

class Character_admin(admin.ModelAdmin):
    pass

admin.site.register(Character, Character_admin)