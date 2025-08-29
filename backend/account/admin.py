from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

# Register your models here.

admin.site.site_header = "Seentax"

UserAdmin.fieldsets[2][1]["fields"] = (
    "is_active",
    "is_staff",
    "is_superuser",
    "groups",
    "user_permissions",
    "point",
)
UserAdmin.list_display += ("point",)

admin.site.register(User, UserAdmin)
