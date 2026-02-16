from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Manager

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    # List view
    list_display = ("email", "role", "is_staff", "is_active")
    list_filter = ("role", "is_staff", "is_active")

    #  Use email instead of username everywhere
    ordering = ("email",)
    search_fields = ("email",)

    # Layout like default Django admin
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "phone", "profile_image")}),
        ("Permissions", {
            "fields": (
                "role",
                "is_active",
                "is_staff",
                "is_superuser",
                "groups",
                "user_permissions",
            )
        }),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",
                "password1",
                "password2",
                "first_name",
                "last_name",
                "phone",
                "profile_image",
                "role",
                "is_staff",
                "is_active",
            ),
        }),
    )

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ("user", "whatsapp", "address")
    search_fields = ("user__email", "whatsapp")