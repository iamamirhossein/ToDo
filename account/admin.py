from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile


def deactivate_profile(modeladmin, request, queryset):
    records = queryset.update(is_active=False)
    message_bit = 'items'
    if records == 1:
        message_bit = 'item'
    modeladmin.message_user(request, f'{records} {message_bit} deactivated.')


deactivate_profile.short_description = 'Deactive Profile'


class ProfileInline(admin.StackedInline):
    model = Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nick_name', 'user', 'is_active')
    actions = [deactivate_profile]


class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', ]
    inlines = [ProfileInline]


admin.site.register(Profile, ProfileAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
