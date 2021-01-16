from django.db.models.fields import TextField
from django.forms import ModelForm, TextInput, DateInput, NumberInput, Select, forms
from django.forms.widgets import Textarea
from .models import Book

class BookCreationForm(ModelForm):
    class Meta:
        model=Book
        fields='__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Book Name'
                }
            ),
            'author': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'description': Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': '3'
                }
            ),
            'published_on': DateInput(
                attrs={
                    'class': 'form-control',
                    'type': 'date'
                }
            ),
            'price': NumberInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'category': Select(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
    
    def clean_category(self):
        category = self.cleaned_data.get('category')
        price = self.cleaned_data.get('price')
        
        if category == 'sports' and price < 250:
            raise forms.ValidationError("Invalid Price for sports")

        return category