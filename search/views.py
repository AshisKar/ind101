from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, TemplateView, DetailView
from django.views.generic.edit import FormView

from .forms import SearchForm
from .models import Scheme


def search(request):
    import ipdb;ipdb.set_trace()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            gender_criteria = form.cleaned_data.get('gender_criteria')
            age_criteria = form.cleaned_data.get('age_criteria')
            oppurtunity = Scheme.objects.filter(gender_criteria=gender_criteria, age_criteria=age_criteria )
            return render(request, 'search/results.html', {'oppurtunity': oppurtunity})
    else:
        form = SearchForm()

        return render(request, 'search/search.html', {'form': form})


# class SearchFormView(FormView):
#     print("inside search form")
#     template_name = 'search/search.html'
#     form_class = SearchForm
#     success_url = '/result/'

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         return super().form_valid(form)

# class ResultFormView(ListView):
#     model = Scheme
#     template_name = 'search/results.html'




