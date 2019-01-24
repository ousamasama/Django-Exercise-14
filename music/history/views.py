from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Artist, Song
from .forms import ArtistForm, SongForm

# Create your views here.

def index(request):
    all_artists = Artist.objects.order_by('artist_name')
    output = { 'all_artists': all_artists }
    return render(request, 'history/index.html', output)

def detail(request, artist_id):
    artist = get_object_or_404(Artist, pk=artist_id)
    return render(request, 'history/detail.html', {'artist': artist})

def add_artist(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ArtistForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            artist = Artist()
            artist.artist_name = form.cleaned_data['artist_name']
            artist.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/artists/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ArtistForm()

    return render(request, 'history/addartist.html', {'form': form})