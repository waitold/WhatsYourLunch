from django.shortcuts import render
from django.shortcuts import render, redirect
from . import models
from django.views import View
from django.views.generic import ListView
from .forms import SearchForm
from . import api_controller
import random
from . import model_controller


class TopView(View):
    def get(self, request, *args, **kwargs):
        store_list = model_controller.get_recent_lunch()
        return render(request, 'search/top.html', {'store_list': list([i['store'], i['address']] for i in store_list)})


class SearchView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'recently_place': model_controller.get_recently_place(),
            'popular_query': models.Query.objects.all().order_by('-keyword').values(),
            'radius': [500, 1000, 2000, 5000],
            'form': SearchForm(),
        }
        return render(request, 'search/index.html', context)

    def post(self, request, *args, **kwargs):
        form = SearchForm(request.POST)
        if not form.is_valid():
            return render(request, 'search/index.html', {'form': form})
        place = form.cleaned_data['place']
        keyword = form.cleaned_data['keyword']
        radius = form.cleaned_data['radius']
        model_controller.create_search(place, keyword, radius)
        model_controller.update_query(keyword)

        loc = api_controller.place_to_ll(place)
        name_loc_dict = api_controller.search_place(loc, keyword, radius)
        random_venue = 0
        rand_adr = 0
        if len(name_loc_dict) > 0:
            rand = random.randrange(0, len(name_loc_dict))
            random_venue = list(name_loc_dict.keys())[rand]
            rand_adr = list(name_loc_dict.values())[rand][1]
        return render(request, 'search/result.html', {'name_loc_dict': name_loc_dict,
                                                      'place': place, 'random': random_venue, 'random_adr': rand_adr})


class ResultView(View):
    def get(self, request, *args, **kwargs):
        context = {
            'recently_place': model_controller.get_recently_place(),
            'popular_query': models.Query.objects.all().order_by('keyword').values(),
            'radius': [500, 1000, 2000, 5000],
            'form': SearchForm(),
        }
        return redirect('../search')

    def post(self, request, *args, **kwargs):
        store_name = request.POST.get('store', None)
        store_adr = request.POST.get('loc', None)
        model_controller.create_lunch(store_name, store_adr)
        context = {
            'store_name': store_name,
            'store_adr': store_adr
        }
        return render(request, 'search/decision.html', context)


top = TopView.as_view()
search = SearchView.as_view()
result = ResultView.as_view()
