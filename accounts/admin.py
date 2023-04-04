# 3.4
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'age', 'is_staff', ] #5.1
    fieldsets = UserAdmin.fieldsets + ( #5.1
        (None, {'fields': ('age',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + ( #5.1
        (None, {'fields': ('age',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
