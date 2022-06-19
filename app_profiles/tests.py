from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Profile


def create_user(username):
    """Creating a test user"""
    user = User.objects.create(username=username)
    user.set_password('P@ssword1')
    return user


def create_profile(user, favorite_city):
    """Creating a test profile"""
    return Profile.objects.create(user=user, favorite_city=favorite_city)


class ViewTests(TestCase):

    def test_index_view(self):
        url = reverse('profiles:profiles_index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<title>Profiles</title>", response.content)

    def test_letting_view(self):
        user = create_user(username='test')
        profile = create_profile(user=user, favorite_city='test city')
        url = reverse('profiles:profile', args=(user.username,))
        response = self.client.get(url)
        title = "<title>{}</title>".format(profile.user.username)
        self.assertEqual(response.status_code, 200)
        self.assertIn(title.encode('utf-8'), response.content)
