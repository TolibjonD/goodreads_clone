from django import forms
from books.models import BookReview


class BookReviewForm(forms.ModelForm):
    stars_given = forms.IntegerField(widget=forms.HiddenInput(attrs={'id':'stars_given', 'value':'0'}))
    class Meta:
        model = BookReview
        fields = ("stars_given", "comment")