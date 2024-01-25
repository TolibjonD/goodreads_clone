import code
from rest_framework.test import APITestCase
from books.models import Book , BookReview
from users.models import CustomUser
from rest_framework.reverse import reverse

class BookReviewAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username="Tolibjon" , first_name="Tolibjon")
        self.user.set_password("Saidkodirov")
        self.user.save()
        self.client.login(username = 'Tolibjon' , password='Saidkodirov')

    def test_book_review_detail(self):
        book = Book.objects.create(title="title1" ,  description="Description1" , isbn = "1111")
        br = BookReview.objects.create(user=self.user , book = book , stars_given=5 , comment = "Very good book")

        response = self.client.get(
            reverse("api:book_review" , kwargs={"id": br.id})
        )

        self.assertEqual(response.status_code , 200)
        self.assertEqual(response.data['id'] , br.id)
        self.assertEqual(response.data['stars_given'] , 5)
        self.assertEqual(response.data['comment'] , br.comment)
        self.assertEqual(response.data['book']['title'] , book.title)
        self.assertEqual(response.data['book']['description'] , book.description)
        self.assertEqual(response.data['user']['username'] , self.user.username)
        self.assertEqual(response.data['user']['first_name'] , self.user.first_name)
        self.assertEqual(response.data['book']['isbn'] , book.isbn)

    def test_book_reviews_list(self):
        book = Book.objects.create(title="title1" ,  description="Description1" , isbn = "1111")
        br1 = BookReview.objects.create(user=self.user , book = book , stars_given=5 , comment = "Very good book")
        br2 = BookReview.objects.create(user=self.user , book = book , stars_given=3 , comment = "Bad book")

        response = self.client.get(reverse("api:book_reviews"))

        self.assertEqual(response.status_code , 200)
        self.assertEqual(response.data['count'] , 2)

        self.assertIn('next' , response.data)
        self.assertIn('previous' , response.data)

        self.assertEqual(response.data['results'][0]['id'] , br1.id)
        self.assertEqual(response.data['results'][0]['stars_given'] , br1.stars_given)
        self.assertEqual(response.data['results'][0]['comment'] , br1.comment)
        self.assertEqual(response.data['results'][1]['id'] , br2.id)
        self.assertEqual(response.data['results'][1]['stars_given'] , br2.stars_given)
        self.assertEqual(response.data['results'][1]['comment'] , br2.comment)

    def test_bookreview_delete(self):
        book = Book.objects.create(title="title1" ,  description="Description1" , isbn = "1111")
        br = BookReview.objects.create(user=self.user , book = book , stars_given=5 , comment = "Very good book")

        res = self.client.delete(reverse("api:book_review", kwargs={"id": br.id}))

        self.assertEqual(res.status_code , 204)
        self.assertFalse(BookReview.objects.filter(id=br.id).exists())

    def test_bookreview_patch(self):
        book = Book.objects.create(title="title1" ,  description="Description1" , isbn = "1111")
        br = BookReview.objects.create(user=self.user , book = book , stars_given=5 , comment = "Very good book")

        response = self.client.patch(reverse("api:book_review" , kwargs={"id": br.id}) , data={'stars_given':4})

        br.refresh_from_db()

        self.assertEqual(response.status_code , 200)
        self.assertEqual(br.stars_given , 4)

    def test_bookreview_put(self):
        book = Book.objects.create(title="title1" ,  description="Description1" , isbn = "1111")
        br = BookReview.objects.create(user=self.user , book = book , stars_given=5 , comment = "Very good book")

        response = self.client.put(
            reverse("api:book_review" , kwargs={"id": br.id}),
            data={
                "stars_given": 2,
                "comment": "Bad book",
                "user_id": self.user.id,
                "book_id": book.id
            }
            )
        br.refresh_from_db()

        self.assertEqual(response.status_code  , 200)
        self.assertEqual(br.comment , "Bad book")
        self.assertEqual(br.stars_given , 2)

    def test_create_bookreview(self):
        book = Book.objects.create(title="title1" ,  description="Description1" , isbn = "1111")

        data = {
            "stars_given": 4,
            "comment": "Nice book",
            "book_id": book.id,
            "user_id": self.user.id
        }

        res = self.client.post(
            reverse("api:book_reviews"),
            data=data
        )

        br = BookReview.objects.get(book=book)

        self.assertEqual(res.status_code , 201)
        self.assertEqual(br.stars_given , 4)
        self.assertEqual(br.comment , "Nice book")