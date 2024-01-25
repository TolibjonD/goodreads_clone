from django.urls import path
from api.views import BookReviewDetailAPIView , BookReviewsAPIView


app_name = "api"
urlpatterns = [
    path("reviews/<int:id>/" , BookReviewDetailAPIView.as_view() , name="book_review"),
    path("reviews/" , BookReviewsAPIView.as_view() , name="book_reviews"),
]
