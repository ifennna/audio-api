import unittest
import string
import random

from app.test.base import BaseTestCase
from app.main.services.audiobooks import AudiobookService
from app.main.errors.errors import ValidationError

class TestAudiobookService(BaseTestCase):
    def test_add_audiobook(self):
        service = AudiobookService()
        audiobook_data = {
            'title': 'test',
            'duration': 100,
            'author': 'generic',
            'narrator': 'generic'
        }
        response = service.add(audiobook_data)

        self.assertIn('status', response)
        self.assertEqual(response['status'], 'success')

    def test_failed_add_audiobook(self):
        service = AudiobookService()

        long_name = ''.join(random.choice(string.ascii_letters) for i in range(101))

        audiobook_data_one = {
            'title': 'test',
            'duration': -1,
            'author': 'generic',
            'narrator': 'generic'
        }
        audiobook_data_two = {
            'title': 'test',
            'duration': 100,
            'author': 'generic',
            'narrator': long_name
        }
        audiobook_data_three = {
            'title': 'test',
            'duration': 100,
            'author': long_name,
            'narrator': 'generic'
        }
        audiobook_data_four = {
            'title': long_name,
            'duration': 100,
            'author': 'generic',
            'narrator': 'generic'
        }

        self.assertRaises(ValidationError, service.add, audiobook_data_one)
        self.assertRaises(ValidationError, service.add, audiobook_data_two)
        self.assertRaises(ValidationError, service.add, audiobook_data_three)
        self.assertRaises(ValidationError, service.add, audiobook_data_four)

    def test_get_audiobook(self):
        service = AudiobookService()
        audiobook_data = {
            'title': 'test',
            'duration': 100,
            'author': 'generic',
            'narrator': 'generic'
        }
        service.add(audiobook_data)
        audiobook = service.get(1)

        self.assertEqual(audiobook.id, 1)
        self.assertEqual(audiobook.title, audiobook_data['title'])

    def test_failed_get_audiobook(self):
        service = AudiobookService()

        self.assertRaises(ValidationError, service.get, 0)

    def test_edit_audiobook(self):
        service = AudiobookService()
        audiobook_data = {
            'title': 'test',
            'duration': 100,
            'author': 'generic',
            'narrator': 'generic'
        }
        service.add(audiobook_data)

        audiobook_data['duration'] = 20
        service.edit(1, audiobook_data)
        audiobook = service.get(1)

        self.assertEqual(audiobook.id, 1)
        self.assertEqual(audiobook.duration, audiobook_data['duration'])

    def test_failed_edit_audiobook(self):
        service = AudiobookService()
        audiobook_data = {
            'title': 'test',
            'duration': 100,
            'author': 'generic',
            'narrator': 'generic'
        }

        self.assertRaises(ValidationError, service.edit, 0, audiobook_data)        



if __name__ == '__main__':
    unittest.main()