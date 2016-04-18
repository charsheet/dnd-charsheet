from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.http import HttpRequest
User = get_user_model()

from google.appengine.ext import testbed

from charsheet.models import Character
from .character_data import character_data

class CharacterViewsTest(TestCase):
    charsheet_data = character_data

    def setUp(self):
        """Initalise GAE test stubs before each test is run."""
        self.testbed = testbed.Testbed()
        self.testbed.activate()

    def tearDown(self):
        """Remove the GAE test subs after each test."""
        self.testbed.deactivate()

    def user_login(self):
        """
        Set user environment variables and initalise the GAE user stub.
        Taken from http://stackoverflow.com/questions/6159396/.
        """

        self.testbed.setup_env(
            USER_EMAIL='admin@example.com',
            USER_ID='12345',
            USER_IS_ADMIN='1',
            overwrite=True,
        )
        self.testbed.init_user_stub()


    def create_character(self):
        self.test_user = User.objects.pre_create_google_user(email='admin@example.com')
        character_data.update({'user': self.test_user})
        character_data.update({'users_with_access': [self.test_user]})
        Character.objects.create(**character_data)

    def test_display_all_characters_logged_in_index(self):
        self.user_login()
        self.create_character()
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('charsheet/index.html')
        self.assertTrue('charsheet_list' in response.context)

        self.assertIn('html', response.content)
        self.assertIn(self.charsheet_data['character_name'], response.content)

class CharacterDetailViewTest(TestCase):
    charsheet_data = character_data
    def setUp(self):

        self.testbed = testbed.Testbed()
        self.testbed.activate()

        self.test_user = User.objects.pre_create_google_user(email='admin@example.com')
        character_data.update({'user': self.test_user})
        character_data.update({'users_with_access': [self.test_user]})
        self.character = Character.objects.create(**character_data)

    def tearDown(self):
        """Remove the GAE test subs after each test."""
        self.testbed.deactivate()

    def user_login(self):
        """
        Set user environment variables and initalise the GAE user stub.
        Taken from http://stackoverflow.com/questions/6159396/.
        """

        self.testbed.setup_env(
            USER_EMAIL='admin@example.com',
            USER_ID='12345',
            USER_IS_ADMIN='1',
            overwrite=True,
        )
        self.testbed.init_user_stub()

    def test_display_character_sheet_detail(self):
        self.user_login()
        resp = self.client.get(reverse('detail', kwargs={'pk': self.character.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'detail.html')
        self.assertIn(self.charsheet_data['character_name'], resp.content)

class CharacterUpdateViewTest(TestCase):
    charsheet_data = character_data
    def setUp(self):

        self.testbed = testbed.Testbed()
        self.testbed.activate()

        self.test_user = User.objects.pre_create_google_user(email='admin@example.com')
        character_data.update({'user': self.test_user})
        character_data.update({'users_with_access': [self.test_user]})
        self.character = Character.objects.create(**character_data)

    def tearDown(self):
        """Remove the GAE test subs after each test."""
        self.testbed.deactivate()

    def user_login(self):
        """
        Set user environment variables and initalise the GAE user stub.
        Taken from http://stackoverflow.com/questions/6159396/.
        """

        self.testbed.setup_env(
            USER_EMAIL='admin@example.com',
            USER_ID='12345',
            USER_IS_ADMIN='1',
            overwrite=True,
        )
        self.testbed.init_user_stub()

    def test_display_character_sheet_detail(self):
        self.user_login()
        resp = self.client.get(reverse('update', kwargs={'pk': self.character.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'update.html')
        self.assertIn(self.charsheet_data['character_name'], resp.content)
