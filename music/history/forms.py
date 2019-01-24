from django import forms

class ArtistForm(forms.Form):
    artist_name = forms.CharField(label="Artist Name", max_length=100)

class SongForm(forms.Form):
    song_name = forms.CharField(label="Artist Name", max_length=100)