from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = '__all__'
        widgets = {
            'published_date': forms.DateInput(attrs={'type': 'date'})
        }
