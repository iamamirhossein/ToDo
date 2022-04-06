from django.contrib import admin
from .models import Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_at', 'modified_at',)
    list_filter = ('status',)


admin.site.register(Item, ItemAdmin)
