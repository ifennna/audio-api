import unittest
import string
import random

from app.test.base import BaseTestCase
from app.main.services.podcasts import PodcastService
from app.main.errors.errors import ValidationError

class TestPodcastService(BaseTestCase):
    def test_add_podcast(self):
        service = PodcastService()

        podcast_data_one = {
            'name': 'test',
            'duration': 100,
            'host': 'generic',
            'participants': []
        }
        podcast_data_two = {
            'name': 'test',
            'duration': 100,
            'host': 'generic'
        }

        response_one = service.add(podcast_data_one)
        response_two = service.add(podcast_data_two)

        self.assertIn('status', response_one)
        self.assertIn('status', response_two)
        self.assertEqual(response_one['status'], 'success')
        self.assertEqual(response_two['status'], 'success')

    def test_failed_add_podcast(self):
        service = PodcastService()

        long_name = ''.join(random.choice(string.ascii_letters) for i in range(101))
        many_participants = []
        many_long_participants = []
        many_participants.extend('person' for i in range(11))
        many_long_participants.extend(long_name for i in range(9))

        podcast_data_one = {
            'name': 'test',
            'duration': 100
        }
        podcast_data_two = {
            'name': 'test',
            'duration': 20,
            'host': long_name,
            'participants': []
        }
        podcast_data_three = {
            'name': 'test',
            'duration': 100,
            'host': 'generic',
            'participants': many_participants
        }
        podcast_data_four = {
            'name': 'test',
            'duration': 100,
            'host': 'generic',
            'participants': many_long_participants
        }

        self.assertRaises(ValidationError, service.add, podcast_data_one)
        self.assertRaises(ValidationError, service.add, podcast_data_two)
        self.assertRaises(ValidationError, service.add, podcast_data_three)
        self.assertRaises(ValidationError, service.add, podcast_data_four)

    def test_get_podcast(self):
        service = PodcastService()
        podcast_data_one = {
            'name': 'test',
            'duration': 100,
            'host': 'generic',
            'participants': []
        }
        podcast_data_two = {
            'name': 'test',
            'duration': 100,
            'host': 'generic',
            'participants': ['generic', 'generic', 'one generic']
        }
        service.add(podcast_data_one)
        service.add(podcast_data_two)
        podcast_one = service.get(1)
        podcast_two = service.get(2)

        self.assertEqual(podcast_one['id'], 1)
        self.assertEqual(podcast_two['id'], 2)
        self.assertEqual(podcast_one['participants'], podcast_data_one['participants'])
        self.assertEqual(podcast_two['participants'], podcast_data_two['participants'])

    def test_failed_get_podcast(self):
        service = PodcastService()

        self.assertRaises(ValidationError, service.get, 0)

    def test_edit_podcast(self):
        service = PodcastService()
        podcast_data = {
            'name': 'test',
            'duration': 100,
            'host': 'generic',
            'participants': []
        }
        service.add(podcast_data)

        podcast_data['duration'] = 20
        service.edit(1, podcast_data)
        podcast = service.get(1)

        self.assertEqual(podcast['id'], 1)
        self.assertEqual(podcast['duration'], podcast_data['duration'])

    def test_failed_edit_podcast(self):
        service = PodcastService()
        podcast_data = {
            'name': 'test',
            'duration': 100
        }

        self.assertRaises(ValidationError, service.edit, 0, podcast_data)        



if __name__ == '__main__':
    unittest.main()