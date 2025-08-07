from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Books, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'})
        }
        
class SearchForm(forms.Form):
    words = forms.CharField(
        label='',
        max_length=50,
        widget=forms.TextInput(attrs={
            'class': 'form-control me-2',
            'placeholder': 'タイトル・著者',
        })
    )
    


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'publisher', 'published_date', 'isbn', 'genre', 'image']
        

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content', 'rating']
