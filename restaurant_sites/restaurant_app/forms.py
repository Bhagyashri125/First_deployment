from django import forms
#from django.forms import ModelForm
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone'}),
            'message': forms.Textarea(attrs={'cols': 20, 'rows': 5,'placeholder': 'Message'})
        }
