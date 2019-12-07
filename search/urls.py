from django.urls import path
from . import views

app_name = 'WhatsYourLunch'
urlpatterns = [
    path('search/', views.search, name='search'),
]
