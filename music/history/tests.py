import unittest
from django.test import TestCase
from django.urls import reverse
from .models import Artist

# Create your tests here.


class ArtistTest(TestCase):
    def test_list_artists(self):
        new_artist = Artist.objects.create(
            artist_name = "Corgi Fur"
        )

        response = self.client.get(reverse('history:index'))

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.context['all_artists']), 1)

        self.assertIn(new_artist.artist_name.encode(), response.content)

    def test_get_artist_form(self):
        response = self.client.get(reverse('history:addartist'))

        self.assertIn(
            '<input type="text" name="artist_name" maxlength="100" required id="id_artist_name">'.encode(), response.content
        )

    def test_post_artist(self):
        response = self.client.post(reverse('history:addartist'), 
            {'artist_name': 'Corgi Fur'})

        self.assertEqual(response.status_code, 302)

    def test_get_artist_detail(self):
        new_artist = Artist.objects.create(
            artist_name = "Corgi Fur"
        )

        response = self.client.get(reverse('history:detail', args=(1,)))
        print("response", response)
        self.assertEqual(response.context["artist"].artist_name, new_artist.artist_name)
