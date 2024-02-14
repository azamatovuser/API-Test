from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Account, Comment
from .forms import AccountCreationForm, AccountChangeForm


class AccountAdmin(BaseUserAdmin):
    form = AccountChangeForm
    add_form = AccountCreationForm
    list_display = ('id', 'username', 'full_name', 'about_me', 'is_superuser', 'is_staff',
                    'is_active', 'date_modified', 'date_created')
    readonly_fields = ('date_modified', 'date_created')
    list_filter = ('date_created', 'is_superuser', 'is_staff', 'is_active')
    ordering = ()
    fieldsets = (
        (None, {'fields': ('username', 'full_name', 'about_me', 'picture', 'password')}),
        (_('Permissions'), {'fields': ('is_superuser', 'is_staff', 'is_active',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('date_modified', 'date_created')}),
    )
    add_fieldsets = (
        (None, {'classes': ('wide',), 'fields': ('username', 'password1', 'password2'), }),
    )
    search_fields = ('username', 'full_name')


admin.site.register(Account, AccountAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'from_account', 'message', 'to_account')
    list_filter = ('from_account', 'to_account')