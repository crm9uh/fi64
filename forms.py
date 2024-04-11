from django import forms
from dataapp.models import Person

class dataappForm(forms.ModelForm):
    additional_field = forms.CharField(max_length=100,required=False)
    class Meta:
        model = Person
        fields = '__all__'