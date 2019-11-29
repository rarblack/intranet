from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.utils.translation import gettext, gettext_lazy as _
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'get_middle_name', 'is_staff',)

    def get_middle_name(self, instance):
        return instance.profile.middle_name

    get_middle_name.short_description = 'Middle name'

    def get_inline_instances(self, request, obj=None):

        if not obj:
            return list()
        return super().get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)



#
# class CustomUserAdmin(UserAdmin):
#     inlines = (ProfileInline, )
#     list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'get_middle_name', 'is_staff',)
#     list_select_related = ('profile', )
#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
#         (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_deputy_to_HEAD','is_HEAD', 'is_deputy_to_GD', 'is_GD', 'is_superuser',
#                                        'groups', 'user_permissions')}),
#         (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2'),
#         }),
#     )

