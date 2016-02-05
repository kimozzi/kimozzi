from django.contrib import admin
from blog.models import Post, Comment, Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']

    def __str__(self):
        return self.title

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)