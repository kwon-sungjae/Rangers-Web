from django.contrib import admin
from .models import Chat

# Register your models here.

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ['id', 'roomname', 'author', 'message', 'create_date', 'vilification']
    list_filter = ['roomname', 'author', 'create_date']
    search_fields = ['roomname', 'author__username', 'message']
    readonly_fields = ['id', 'create_date']
    fieldsets = [
        (None, {'fields': ['id', 'create_date']}),
        ('Chat Details', {'fields': ['roomname', 'author', 'message', 'vilification']}),
    ]
    ordering = ['-create_date']