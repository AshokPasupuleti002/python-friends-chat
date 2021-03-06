from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'birthday', 'email', 'favouriteURL', 'desc')

# Register your models here.
admin.site.register(Person, PersonAdmin)


