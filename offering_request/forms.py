from django import forms

from .models import Offering_request


class Offering_requestForm(forms.ModelForm):
    class Meta:
        model = Offering_request
        fields = '__all__'
