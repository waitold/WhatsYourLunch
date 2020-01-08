from django.urls import path
from . import views

app_name = 'WhatsYourLunch'
urlpatterns = [
    path('', views.top, name='top'),
    path('search/', views.search, name='search'),
    path('result/', views.result, name='result')
]
