import unittest

from app.test.base import BaseTestCase
from app.main.services.songs import SongService
from app.main.errors.errors import ValidationError

class TestSongService(BaseTestCase):
    def test_add_song(self):
        service = SongService()
        song_data = {
            'name': 'test',
            'duration': 100
        }
        response = service.add(song_data)

        self.assertIn('status', response)
        self.assertEqual(response['status'], 'success')

    def test_failed_add_song(self):
        service = SongService()
        song_data_one = {
            'duration': 100
        }
        song_data_two = {
            'name': 'test',
            'duration': -1
        }
        song_data_three = {}

        self.assertRaises(ValidationError, service.add, song_data_one)
        self.assertRaises(ValidationError, service.add, song_data_two)
        self.assertRaises(ValidationError, service.add, song_data_three)

    def test_get_song(self):
        service = SongService()
        song_data = {
            'name': 'test',
            'duration': 100
        }
        service.add(song_data)
        song = service.get(1)

        self.assertEqual(song.id, 1)
        self.assertEqual(song.name, song_data['name'])

    def test_failed_get_song(self):
        service = SongService()

        self.assertRaises(ValidationError, service.get, 0)

    def test_edit_song(self):
        service = SongService()
        song_data = {
            'name': 'test',
            'duration': 100
        }
        service.add(song_data)

        song_data['duration'] = 20
        service.edit(1, song_data)
        song = service.get(1)

        self.assertEqual(song.id, 1)
        self.assertEqual(song.duration, song_data['duration'])

    def test_failed_edit_song(self):
        service = SongService()
        song_data = {
            'name': 'test',
            'duration': 100
        }

        self.assertRaises(ValidationError, service.edit, 0, song_data)        



if __name__ == '__main__':
    unittest.main()