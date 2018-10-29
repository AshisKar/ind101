from django import forms

from .models import Scheme


class SearchForm(forms.ModelForm):
    caste = forms.CharField()

    class Meta:
        model = Scheme
        fields = ['age_criteria', 'gender_criteria','annual_income_range', 'source_of_livelihood']
