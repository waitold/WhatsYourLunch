import foursquare
import googlemaps
import json
from . import api_key


def search_venues_info(ll, radius, query):
    client = foursquare.Foursquare(client_id=api_key.CLIENT_ID, client_secret=api_key.CLIENT_SECRET)
    params = dict(
        ll=ll,
        intent='browse',
        radius=radius,
        query=query,
    )
    res = client.venues.search(params=params)
    with open('result.txt', mode='w') as f:
        f.write(json.dumps(res, indent=2).encode().decode('unicode-escape'))
    return {i['name']: i['id'] for i in res['venues']}


def place_to_ll(place):
    gmaps = googlemaps.Client(key=api_key.GOOGLE_API_KEY)
    geocode = gmaps.geocode(place)
    lat = str(geocode[0]["geometry"]["location"]["lat"])
    lng = str(geocode[0]["geometry"]["location"]["lng"])
    return lat+','+lng


def search_place(loc, keyword, rad):
    gmaps = googlemaps.Client(key=api_key.GOOGLE_API_KEY)
    res = gmaps.places_nearby(loc, rad, keyword, 'ja')
    with open('g_result.txt', mode='w') as f:
        f.write(json.dumps(res, indent=2).encode().decode('unicode-escape'))
    name_list = ["".join(i['name'].split()) for i in res['results']]
    geo_list = [i['geometry']['location'] for i in res['results']]
    loc_list = [str(geo['lat'])+','+str(geo['lng']) for geo in geo_list]
    adr_list = [i['vicinity'] for i in res['results']]
    return{name_list[i]: [loc_list[i], adr_list[i]] for i in range(len(name_list))}


def search_id(keyword):
    gmaps = googlemaps.Client(key=api_key.GOOGLE_API_KEY)
    res = gmaps.places_autocomplete(keyword)
    with open('place_detail.txt', mode='w') as f:
        f.write(json.dumps(res, indent=2).encode().decode('unicode-escape'))
