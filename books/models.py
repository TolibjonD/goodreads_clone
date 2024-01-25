from django.utils import timezone
from django.db import models
from users.models import CustomUser
from django.core.validators import MinValueValidator , MaxValueValidator

# Create your models here.
# * MODEL _ 1
class Book(models.Model):
    title = models.CharField(max_length = 250)
    description = models.TextField()
    isbn = models.CharField(max_length = 17)
    cover_picture = models.ImageField(upload_to="books/" , default="default_cover_picture.jpg")

    def __str__(self) -> str:
        return self.title

# * MODEL _ 2
class Author(models.Model):
    first_name = models.CharField(max_length = 120)
    last_name = models.CharField(max_length = 120)
    email = models.EmailField()
    bio = models.TextField()

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    
# * MODEL _ 3
class BookAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete = models.CASCADE)
    author = models.ForeignKey(Author, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f"{self.author.first_name} - {self.book.title}"
    

# * MODEL _ 4
class BookReview(models.Model):
    user = models.ForeignKey(CustomUser, on_delete = models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    comment = models.TextField()
    stars_given = models.IntegerField(validators = [MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(default = timezone.now)

    def __str__(self) -> str:
        return f"{self.user.username} left comment for {self.book.title}."
    
