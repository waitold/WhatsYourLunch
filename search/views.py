from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import SearchForm
from . import api_controller
# Create your views here.


class SearchView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'form': SearchForm(),
        }
        return render(request, 'search/index.html', context)

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if not form.is_valid():
            return render(request, 'search/index.html', {'form': form})
        ll = api_controller.place_to_ll(form.cleaned_data['place'])
        name_id_dict = api_controller.search_venues_info(ll, form.cleaned_data['radius'], form.cleaned_data['query'])
        return render(request, 'search/result.html', {'result': name_id_dict})


search = SearchView.as_view()
