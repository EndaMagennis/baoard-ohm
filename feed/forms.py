from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    '''Form to create a new post'''
    class Meta:
        model = Post
        # add image field to form
        fields = ('title', 'content', 'image',
                  'genre', 'number_of_players', 'age_range',
                  'play_time', 'experience', 'price_range',
                  'rating', )
