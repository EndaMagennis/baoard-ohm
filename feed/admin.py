from django.contrib import admin
from .models import Post
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
