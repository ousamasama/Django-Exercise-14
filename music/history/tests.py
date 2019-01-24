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


