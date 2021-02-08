from django.urls import path
from .views import home, sorter

app_name = 'panel'
urlpatterns = [
    path('', home, name='home'),
    path('sorter/', sorter, name='sorter')
]
