from django import forms

from .models import Scheme


class SearchForm(forms.ModelForm):
    caste = forms.CharField()

    class Meta:
        model = Scheme
        fields = ['age', 'gender', 'annual_income_range', 'source_of_livelihood']


    def clean(self):
        cleaned_data = super(SearchForm, self).clean()
        age_criteria = cleaned_data.get('age')
        gender_criteria = cleaned_data.get('gender')
        annual_income_range = cleaned_data.get('annual_income_range')
        source_of_livelihood = cleaned_data.get('source_of_livelihood')
        if not age_criteria and not gender_criteria and not annual_income_range:
            raise forms.ValidationError('You have to write something!')
