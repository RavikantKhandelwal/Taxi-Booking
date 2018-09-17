from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'password', 'credit_card', 'contact', 'email')


admin.site.register(User, UserAdmin)
