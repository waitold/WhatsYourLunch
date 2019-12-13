from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import SearchForm
from . import api_controller
import random
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
        loc = api_controller.place_to_ll(form.cleaned_data['place'])
        name_id_dict = api_controller.search_venues_info(loc, form.cleaned_data['radius'], form.cleaned_data['query'])
        random_venue = 0
        if len(name_id_dict.keys()) > 0:
            random_venue = list(name_id_dict.keys())[random.randrange(0, len(name_id_dict.keys()))]
        api_controller.search_id(random_venue)
        return render(request, 'search/result.html', {'name_id_dict': name_id_dict, 'random': random_venue})


search = SearchView.as_view()
