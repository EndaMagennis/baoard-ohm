from django.contrib import admin
from .models import Post, Like
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    '''Admin View for Post'''

    list_display = ('title', 'slug', 'created_on', )
    search_fields = ['title', 'content', 'genre', 'age_range', 'rating']
    list_filter = ('created_on', )
    prepopulated_fields = {'slug': ('title',)}
    summernote_feilds = ('content',)


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    '''Admin View for Like'''

    list_display = ('user', 'post', )
    search_fields = ['user', 'post']
    list_filter = ('post', )
