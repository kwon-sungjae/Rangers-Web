from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User

# Register your models here.

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('name', 'email', 'nickname', 'is_artist', 'is_admin', 'is_superuser', 'is_staff')
    list_filter = ('is_admin',)

    # admin 페이지에서 수정할때 폼
    fieldsets = (
        (None, {'fields': ('name','email', 'password','nickname',)}),
        ('Personal info', {'fields': ('agency', 'artistgroup', 'profileimage')}),
        ('Permissions', {'fields': ('is_admin','is_superuser','is_staff','is_artist','counting')}),
    )

    # admin 페이지에서 추가할때 폼
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', 'email', 'nickname', 'password1', 'password2', 'is_admin','is_superuser','is_staff')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)