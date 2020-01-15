from . import models


def create_search(place: str, keyword: str, radius: str):
    search = models.Search(place=place, keyword=keyword, radius=radius)
    search.save()


def get_recently_place():
    model = models.Search.objects.all().order_by('-id').values()
    place_list = []
    for place in model.values("place"):
        if place not in place_list:
            place_list.append(place)
        if len(place_list) > 4:
            return place_list
    return place_list


def update_query(keyword: str):
    if models.Query.objects.filter(keyword=keyword).exists():
        model = models.Query.objects.get(keyword=keyword)
        model.overall_count = model.overall_count + 1
        model.recent_count = model.recent_count + 1
        model.save()
    else:
        model = models.Query(keyword=keyword, overall_count=1, recent_count=1)
        model.save()


def create_result(stores: list, place: str, keyword: str, radius: str):
    stores = ','.join(stores)
    model = models.Result(search=models.Search.objects.get(place=place, keyword=keyword, radius=radius), stores=stores)
    model.save()


def create_lunch(store: str, adr: str):
    model = models.YourLunch(store=store, address=adr)
    model.save()


def get_recent_lunch():
    model = models.YourLunch.objects.order_by('-id').values()[:10]
    return model
