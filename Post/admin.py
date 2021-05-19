from django.contrib import admin
from Post.models import Post

# Register your models here.
@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('id', 'post_title', 'post_content', 'post_type', 'post_datetime', 'post_additionalContext')
