from django.shortcuts import render
from books.models import BookReview
from django.core.paginator import Paginator


# * METHOD => GET
# ! ALLOW => ANY USER
# ? PATH => '/'
def landing_page(request):
    return render(request, "landing_page.html")


def home_page(request):
    reviews = BookReview.objects.all().order_by("-created_at")
    for review in reviews:
        review.stars_given = [ star for star in range(review.stars_given) ]
    
    paginator = Paginator(reviews, 4)
    page = request.GET.get('page', 1)
    paginated_page = paginator.get_page(page)
    context = {
        "reviews": paginated_page
    }
    return render(request,'home_page.html', context)