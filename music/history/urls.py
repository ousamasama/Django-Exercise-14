from django.urls import path

from . import views

app_name = 'history'
urlpatterns = [
    # ex: /artists/
    path('', views.index, name='index'),
    # ex: /artists/5/
    path('<int:artist_id>/', views.detail, name='detail'),
    path('addartist/', views.add_artist, name='addartist'),
    path('addsong/', views.add_song, name='addsong')
]