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
        labels = {
            'title': 'Title',
            'content': 'Content',
            'image': 'Image (If no image is selected, a default image will be used)',
            'genre': 'Genre',
            'number_of_players': 'Number of Players',
            'age_range': 'Age Range',
            'play_time': 'Play Time',
            'experience': 'Experience',
            'price_range': 'Price Range',
            'rating': 'Rating',
        }
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control',}),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'number_of_players': forms.Select(attrs={'class': 'form-control'}),
            'age_range': forms.Select(attrs={'class': 'form-control'}),
            'play_time': forms.Select(attrs={'class': 'form-control'}),
            'experience': forms.Select(attrs={'class': 'form-control'}),
            'price_range': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
        }
