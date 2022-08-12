from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'modified')
    list_display = ('title', 'created', 'modified')
    date_hierarchy = 'created'


admin.site.register(Post, PostAdmin)
