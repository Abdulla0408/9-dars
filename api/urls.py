from django.urls import path
from .views import *

app_name = 'api'
urlpatterns = [
    path('service_list/', service_list),
]