from django.urls import path
from .views import index

app_name = 'landing'

urlpatterns = [
    path('', index, name='index'),
]