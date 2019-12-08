import foursquare
import googlemaps
import json
from . import info


def search_venues(ll, radius, query):
    client = foursquare.Foursquare(client_id=info.CLIENT_ID, client_secret=info.CLIENT_SECRET)
    params = dict(
        ll=ll,
        radius=radius,
        query=query,
    )
    res = client.venues.search(params=params)
    return [i['name'] for i in res['venues']]


def place_to_ll(place):
    gmaps = googlemaps.Client(key=info.GOOGLE_API_KEY)
    geocode = gmaps.geocode(place)
    lat = str(geocode[0]["geometry"]["location"]["lat"])
    lng = str(geocode[0]["geometry"]["location"]["lng"])
    return lat+','+lng
