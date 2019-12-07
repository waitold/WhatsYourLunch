from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from .forms import SearchForm
import foursquare
from . import info
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
        ll = '35.690,140.021'
        res = self.search_venues(ll, form.cleaned_data['radius'], form.cleaned_data['query'])
        return render(request, 'search/result.html', {'result': res})

    @classmethod
    def search_venues(cls, ll, radius, query):
        client = foursquare.Foursquare(client_id=info.CLIENT_ID, client_secret=info.CLIENT_SECRET)
        params = dict(
            ll=ll,
            radius=radius,
            query=query,
        )
        res = client.venues.search(params=params)
        print(res)
        return [i['name'] for i in res['venues']]


search = SearchView.as_view()
