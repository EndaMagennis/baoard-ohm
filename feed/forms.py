from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    '''Form to create a new post'''
    class Meta:
        model = Post
        fields = ('title', 'content',
                  'genre', 'number_of_players', 'age_range',
                  'play_time', 'experience', 'price_range',
                  'rating', )
