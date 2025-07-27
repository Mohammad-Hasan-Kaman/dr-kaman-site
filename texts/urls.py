from django.urls import path
from . import views

app_name = 'texts'
urlpatterns = [
    path('', views.text_list, name='text_list'),
]