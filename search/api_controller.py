import foursquare
import googlemaps
from . import api_key


def search_venues_info(ll, radius, query):
    client = foursquare.Foursquare(client_id=api_key.CLIENT_ID, client_secret=api_key.CLIENT_SECRET)
    params = dict(
        ll=ll,
        radius=radius,
        query=query,
        limit=10,
    )
    res = client.venues.search(params=params)
    return {i['name']: i['id'] for i in res['venues']}


def place_to_ll(place):
    gmaps = googlemaps.Client(key=api_key.GOOGLE_API_KEY)
    geocode = gmaps.geocode(place)
    lat = str(geocode[0]["geometry"]["location"]["lat"])
    lng = str(geocode[0]["geometry"]["location"]["lng"])
    return lat+','+lng


