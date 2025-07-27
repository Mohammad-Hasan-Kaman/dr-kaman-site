from django.urls import path
from . import views

app_name = 'audios'
urlpatterns = [
    path('', views.audio_list, name='audio_list'),
]