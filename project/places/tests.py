from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from places.models import Place


class PlacesModelTests(TestCase):
    def setUp(self):
        self.second_user = User.objects.create_user(username='second_user', password='1234')
        self.first_user_instance = {'username': 'first_user', 'password': '1234kjsakdjalskdjqw'}
        self.first_user = User.objects.create_user(**self.first_user_instance)
        self.place = Place.objects.create(
            title='some title',
            text='some text',
            lat=11.11,
            lng=22.22,
            user=self.first_user,
        )
        self.places_count = Place.objects.count()

    def test_home_without_login(self):
        """
        Редирект если пользователь без логина.
        """
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_login_with_username_and_password(self):
        """
        Тест логина с существующими данными.
        """
        client = Client()
        user_login = client.login(**self.first_user_instance)
        self.assertTrue(user_login)

    def test_home_without_places(self):
        """
        Тест пользователя без воспоминаний.
        """
        client = Client()
        client.login(username='second_user', password='1234')
        url = reverse('home')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['places'])

    def test_home(self):
        """
        Тест пользователя с воспоминаниями.
        """
        client = Client()
        client.login(**self.first_user_instance)
        url = reverse('home')
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['places']), self.places_count)

    def test_create_place(self):
        """
        Тест создания воспоминания.
        """
        client = Client()
        client.login(**self.first_user_instance)
        create_place_url = reverse('create-place')
        place = {'title': 'second place', 'text': 'some text', 'lat': 33.33, 'lng': 44.44, 'user': self.first_user}
        create_place_response = client.post(create_place_url, place)
        home_url = reverse('home')
        home_response = client.get(home_url)
        self.assertEqual(create_place_response.status_code, 302)
        self.assertEqual(home_response.status_code, 200)
        self.assertEqual(len(home_response.context['places']), self.places_count + 1)

    def test_place_detail(self):
        """
        Тест одного определенного воспоминания.
        """
        client = Client()
        client.login(**self.first_user_instance)
        place_id = self.place.id
        place_detail_url = reverse('place-detail', args=[place_id])
        place_detail_response = client.get(place_detail_url)
        self.assertEqual(place_detail_response.status_code, 200)
        self.assertEqual(place_detail_response.context['place'], self.place)






