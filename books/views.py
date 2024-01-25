from django.contrib import messages
from click import edit
from django.shortcuts import redirect, render
from django.urls import  reverse
from .models import Book, BookReview
from django.views import View
from django.views.generic import ListView , DetailView
from django.core.paginator import Paginator
from .forms import BookReviewForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

"""class BooksListPageView(ListView):
    queryset = Book.objects.all()
    context_object_name = 'books'
    template_name='books/books__list.html' 
"""

"""class BookDetailPageView(DetailView):
    model = Book
    template_name='books/detail.html'
    pk_url_kwarg = "id"
"""

class BooksListPageView(View):
    def get(self, request):
        books = Book.objects.all().order_by("-id")
        search_query = request.GET.get('q', '')
        if search_query:
            is_paginated = False
            books = Book.objects.all().filter(title__icontains=search_query)
            objects_count = books.count()
            context = {
                "is_paginated": is_paginated,
                "objects_count": objects_count,
                "books": books,
                "q": search_query
            }
            return render(request , "books/books__list.html" , context)
        page = request.GET.get('page')
        paginator = Paginator(books, 2)
        books = paginator.get_page(page)
        is_paginated = True
        context = {
                "is_paginated": is_paginated,
                "books": books,
                "q": search_query
            }
        return render(request , "books/books__list.html" , context)
    
class BookDetailPageView(View):
    def get(self, request, id):
        book = Book.objects.get(id = id)
        reviews = BookReview.objects.filter(book=book).order_by("-id")
        for review in reviews:
            review.stars_given = [ star for star in range(review.stars_given) ]
        
        review_form = BookReviewForm()
        context = {
            "book": book,
            "reviews": reviews,
            "review_form": review_form
        }
        return render(request , "books/detail.html" , context)

class BookReviewEdit(LoginRequiredMixin , View):
    def get(self, request, book_id, review_id):
        book  = Book.objects.get(id=book_id)
        review = book.reviews.get(id=review_id)
        edit_form = BookReviewForm(instance=review)
        return render(request , "books/review_edit.html" , {"form": edit_form, "book": book, "review": review})
    
    def post(self, request, book_id, review_id):
        book = Book.objects.get(id=book_id)
        review = book.reviews.get(id=review_id)
        edit_form = BookReviewForm(instance=review , data=request.POST)
        if edit_form.is_valid():
            edit_form.save()
            return redirect(reverse("books:detail", kwargs={"id": book.id}) + f"#{review.id}")
        else:
            return render(request , "books/review_edit.html" , {"form": edit_form, "book": book, "review": review})
        
class ReviewDeleteConfirmation(LoginRequiredMixin , View):
    def get(self, request , book_id , review_id):
        book = Book.objects.get(id=book_id)
        review = book.reviews.get(id=review_id)
        return render(request , "books/review_delete_confirmatio.html", {"review": review})
    
class DeleteBook(LoginRequiredMixin , View):
    def get(self , request, book_id , review_id):
        book = Book.objects.get(id=book_id)
        review = book.reviews.get(id=review_id)
        review.delete()
        messages.success(request , "You have successfully deleted review !")
        return redirect(reverse("books:detail" , kwargs={"id": book.id}))
    
class GoToRightReviewPlaceView(LoginRequiredMixin , View):
    def get(self, request, book_id , review_id):
        book = Book.objects.get(id=book_id)
        review = book.reviews.get(id = review_id)
        return redirect(reverse("books:detail", kwargs={"id": book.id}) + f"#{review.id}")



class BookReviewView(LoginRequiredMixin, View):
    def post(self, request, id):
        review_form = BookReviewForm(data=request.POST)
        book = Book.objects.get(id=id)
        if review_form.is_valid():
            review = BookReview.objects.create(
                user = request.user,
                book = book,
                comment = review_form.cleaned_data['comment'],
                stars_given = review_form.cleaned_data['stars_given']
            )
            review.save()
            return redirect(reverse("books:detail", kwargs={"id": book.id}))
        return render(request , "books/detail.html" , {"book": book, "review_form": review_form})