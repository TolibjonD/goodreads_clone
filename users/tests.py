from django.test import TestCase
from users.models import CustomUser
from django.urls import reverse
from django.contrib.auth import get_user

# Create your tests here.
class TestCaseRegistration(TestCase):
    def test_user_is_created(self):
        res = self.client.post(
            reverse("users:register"),
            data={
                "username": "tolibjon",
                "first_name": "Tolibjon",
                "last_name": "Saidkodirov",
                "email": "stolibjon123@gmail.com",
                "password": "somepassword"
            }
        )

        user = CustomUser.objects.get(username = "tolibjon")

        self.assertEqual(user.first_name , "Tolibjon")
        self.assertEqual(user.last_name , "Saidkodirov")
        self.assertEqual(user.email , "stolibjon123@gmail.com")
        self.assertNotEqual(user.password , "somepassword")
        self.assertTrue(user.check_password("somepassword"))

    def test_required_fields(self):
        res = self.client.post(
            reverse("users:register"),
            data= {
                    "first_name": "Tolibjon",
                    "email": "tolibjon@mail.ru"
            }
        )

        users_count = CustomUser.objects.count()

        self.assertEqual(users_count , 0)
        self.assertFormError(res , "form", "username", 'This field is required.')
        self.assertFormError(res , "form", "password", 'This field is required.')

    def test_invalid_email(self):
        res = self.client.post(
            reverse("users:register"),
            data={
                "username": "tolibjon",
                "first_name": "Tolbjon",
                "last_name": "Saidkodirov",
                "email": "Invalid-email",
                "password": "somepassword"
            }
        )

        users_count = CustomUser.objects.count()

        self.assertEqual(users_count , 0)
        self.assertFormError(res , "form", "email" , "Enter a valid email address.")

    def test_unique_username(self):
        res1 = self.client.post(
            reverse("users:register"),
            data={
                "username": "tolibjon",
                "first_name": "Tolibjon",
                "last_name": "Saidkodirov",
                "email": "tolibjon@mail.ru",
                "password": "anypassword"
            }
        )
        res2 = self.client.post(
            reverse("users:register"),
            data= {
                "username": "tolibjon",
                "first_name": "Tolibjon",
                "last_name": "Saidkodirov",
                "email": "tolibjon@mail.ru",
                "password": "anypassword"
            }
        )

        users_count = CustomUser.objects.count()

        self.assertEqual(users_count , 1)
        self.assertFormError(res2 , "form", "username" , "A user with that username already exists.")

class TestCaseLogin(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username = "Tolibjon", first_name = "Tolibjon")
        self.user.set_password("somepassword")
        self.user.save()
        
    def test_successfully_login(self):
        self.client.post(
            reverse("users:login"),
            data={
                "username": "Tolibjon",
                "password": "somepassword"
            }
        )

        loged_in_user = get_user(self.client)
        self.assertTrue(loged_in_user.is_authenticated)

    def test_wrong_login_data(self):
        self.client.post(
            reverse("users:login"),
            data={
                "username": "Invalid-username",
                "password": "somepassword"
            }
        )

        loged_in_user = get_user(self.client)
        self.assertFalse(loged_in_user.is_authenticated)

        self.client.post(
            reverse("users:login"),
            data={
                "username": "Tolibjon",
                "password": "Wrong-Password"
            }
        )

        loged_in_user = get_user(self.client)
        self.assertFalse(loged_in_user.is_authenticated)

    def test_logout(self):
        self.client.login(username = "Tolibjon", password="somepassword")
        self.client.get(reverse("users:logout"))
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

class TestCaseProfilePage(TestCase):
    def test_login_required(self):
        res = self.client.get(reverse("users:profile"))

        self.assertEqual(res.status_code , 302)
        self.assertEqual(res.url , reverse("users:login") + "?next=/users/profile/")

    def test_profile_details(self):
        user = CustomUser.objects.create(
            username = "Saidkodirov",
            first_name = "Tolibjon",
            last_name = "Saidkodirov",
            email = "tolibjon@mail.ru"
        )
        user.set_password("somepassword")
        user.save()

        self.client.login(username="Saidkodirov" , password="somepassword")

        res = self.client.get(reverse("users:profile"))

        self.assertContains(res, user.username)
        self.assertContains(res, user.first_name)
        self.assertContains(res, user.last_name)
        self.assertContains(res, user.email)

    def test_update_user_profile(self):
        user = CustomUser.objects.create(
            username = "Saidkodirov",
            first_name = "Tolibjon",
            last_name = "Saidkodirov",
            email = "tolibjon@mail.ru"
        )
        user.set_password("somepassword")
        user.save()

        self.client.login(username="Saidkodirov" , password="somepassword")

        response = self.client.post(
            reverse("users:profile_update"),
            data={
                "username": "Saidkodirov2",
                "first_name": "Tolibjon",
                "last_name": "Saidkodirov",
                "email": "tolibjon2@mail.ru"
            }
        )

        user.refresh_from_db()

        self.assertEqual(user.username , "Saidkodirov2")
        self.assertEqual(user.email , "tolibjon2@mail.ru")

        self.assertEqual(response.url , reverse("users:profile"))