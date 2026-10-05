from django import forms
from django.db.transaction import clean_savepoints

from .models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"