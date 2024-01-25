from django.contrib import admin
from .models import (
    Book,
    BookAuthor,
    Author,
    BookReview
)

# * CREATE MY MODEL ADMINS HERE
class AdminBook(admin.ModelAdmin):
    search_fields = ("title")

class AdminAuthor(admin.ModelAdmin):
    search_fields = ("first_name", "last_name")

class AdminBookAuthor(admin.ModelAdmin):
    pass

class AdminBookReview(admin.ModelAdmin):
    pass

# ? REGISTERING MY MODELS HERE
admin.site.register(Book, AdminAuthor)
admin.site.register(Author, AdminAuthor)
admin.site.register(BookAuthor, AdminBookAuthor)
admin.site.register(BookReview, AdminBookReview)
