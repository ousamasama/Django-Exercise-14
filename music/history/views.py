from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Artist, Song

# Create your views here.

def index(request):
    all_artists = Artist.objects.order_by('artist_name')
    output = ', '.join([a.artist_name for a in all_artists])
    return HttpResponse(output)

def detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'history/detail.html', {'artist': artist})