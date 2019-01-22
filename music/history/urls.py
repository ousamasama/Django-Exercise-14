from django.urls import path

from . import views

urlpatterns = [
    # ex: /artists/
    path('', views.index, name='index'),
    # ex: /artists/5/
    path('<int:artist_id>/', views.detail, name='detail'),
]