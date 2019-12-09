from django import forms


class SearchForm(forms.Form):
    place = forms.CharField(
        label='地名',
        max_length=255,
    )

    query = forms.CharField(
        label='キーワード',
        max_length=255
    )

    radius = forms.IntegerField(
        label='検索半径',
        min_value=100,
        max_value=100000,
    )
