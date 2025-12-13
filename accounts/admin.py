from django.contrib import admin
from .models import User, Manager, PasswordReset
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "email", "role", "is_staff")
    search_fields = ("username", "email")
    ordering = ("username",)

    fieldsets = UserAdmin.fieldsets + (
        ("Custom Fields", {"fields": ("role", "phone", "profile_image")}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Custom Fields", {"fields": ("role", "phone", "profile_image")}),
    )


admin.site.register(User, CustomUserAdmin)
admin.site.register(Manager)
admin.site.register(PasswordReset)
