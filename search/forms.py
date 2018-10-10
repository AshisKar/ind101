from django import forms

from .models import Opportunity


class SearchForm(forms.ModelForm):
    caste = forms.CharField()
    annual_income = forms.CharField()

    class Meta:
        model = Opportunity
        fields = ['age_criteria', 'gender_criteria','annual_income_range', 'source_of_livelihood']
