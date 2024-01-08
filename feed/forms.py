from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'content',
                  'genre', 'number_of_players', 'age_range',
                  'play_time', 'experience', 'price_range',
                  'rating', )
