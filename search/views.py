from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, TemplateView

from .forms import SearchForm
from .models import Scheme


# def search(request):
#     if request.method == 'POST':
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             gender_criteria = form.cleaned_data.get('gender_criteria')
#             age_criteria = form.cleaned_data.get('age_criteria')
#             oppurtunity = Opportunity.objects.filter(gender_criteria=gender_criteria, age_criteria=age_criteria )
#             return render(request, 'results.html', {'oppurtunity': oppurtunity})
#     else:
#         form = SearchForm()
#
#         return render(request, 'search/search.html', {'form': form})

class SearchFormView(TemplateView):
    template_name = 'search/search.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = SearchForm()
        context['form'] = form
        return self.render_to_response(context)


class ResultsView(ListView):
    template_name = 'results.html'

    # def get_queryset(self):
    #     return Scheme.objects.filter(gender_criteria=gender_criteria, age_criteria=age_criteria )
