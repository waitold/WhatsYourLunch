from django import forms
from .models import YourLunch


class SearchForm(forms.Form):
    place = forms.CharField(
        label='どこで？',
        max_length=31,
    )

    keyword = forms.CharField(
        label='何食べる？',
        max_length=15
    )

    radius = forms.IntegerField(
        label='検索半径(m)',
        min_value=100,
        max_value=100000,
    )
