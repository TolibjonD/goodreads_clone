from django.urls import path
from .views import (
                    BooksListPageView , 
                    BookDetailPageView, 
                    BookReviewView, 
                    BookReviewEdit,
                    GoToRightReviewPlaceView,
                    ReviewDeleteConfirmation,
                    DeleteBook
)

app_name = "books"
urlpatterns = [
    path("", BooksListPageView.as_view(), name="books"),
    path("<int:id>/detail/", BookDetailPageView.as_view(), name="detail"),
    path("<int:id>/reviews", BookReviewView.as_view(), name="reviews"),
    path("<int:book_id>/gotoreview/<int:review_id>/", GoToRightReviewPlaceView.as_view(), name="gotoreview"),
    path("<int:book_id>/edit/<int:review_id>/", BookReviewEdit.as_view(), name="review_edit"),
    path("<int:book_id>/ReviewDeleteConfirmation/<int:review_id>/", ReviewDeleteConfirmation.as_view(), name="review_delete_confirm"),
    path("<int:book_id>/delete/<int:review_id>/", DeleteBook.as_view(), name="delete_review")
]
