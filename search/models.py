from django.db import models


class Search(models.Model):
    place = models.CharField(verbose_name='場所', max_length=15)
    keyword = models.CharField(verbose_name='検索ワード', max_length=31)
    radius = models.IntegerField(verbose_name='検索半径')


class Query(models.Model):
    keyword = models.CharField(verbose_name='場所', max_length=31)
    overall_count = models.IntegerField(verbose_name='全体の検索回数')
    recent_count = models.IntegerField(verbose_name='最近の検索回数')


class Result(models.Model):
    search = models.OneToOneField(Search, verbose_name='検索', on_delete=models.CASCADE)
    stores = models.CharField(verbose_name='検索結果', null=True, max_length=31)


class YourLunch(models.Model):
    store = models.CharField(verbose_name='お店', max_length=31)
