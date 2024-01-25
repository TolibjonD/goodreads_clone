from rest_framework.views import APIView
from .serializers import BookReviewSerializer
from books.models import BookReview
from  rest_framework.response import Response
from rest_framework import status
from users.models import CustomUser
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import viewsets


# Create your views here.


# class BookReviewViewSet(viewsets.ModelViewSet):
#     permission_classes = [IsAuthenticated ]
#     serializer_class = BookReviewSerializer
#     queryset = BookReview.objects.all().order_by('-created_at')
#     lookup_field = "id"

class BookReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BookReviewSerializer
    queryset = BookReview.objects.all()
    lookup_field = "id"
    
    # def get(self, request, id):
    #     try:
    #         book_review = BookReview.objects.get(id=id)
    #         serializer = BookReviewSerializer(book_review)
    #         return Response(data=serializer.data, status=status.HTTP_200_OK)
    #     except:
    #         return Response(data={"message": "Content not found"}, status=status.HTTP_404_NOT_FOUND)    
    
    # def delete(self, request , id):
    #     book_review = BookReview.objects.get(id=id)
    #     comment = book_review.comment
    #     book_review.delete()
    #     data = {
    #         "message": "You successfully delete this review",
    #         "review_comment": comment
    #     }
    #     return Response(data=data , status=status.HTTP_204_NO_CONTENT)  
    
    # def put(self , request , id):
    #     book_review = BookReview.objects.get(id=id)
    #     serializer = BookReviewSerializer(instance=book_review , data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    # def patch(self , request , id):
    #     book_review = BookReview.objects.get(id=id)
    #     serializer = BookReviewSerializer(instance=book_review , data=request.data , partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class BookReviewsAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated ]
    serializer_class = BookReviewSerializer
    queryset = BookReview.objects.all().order_by('-created_at')
    # def get(self , request):
    #     book_reviews = BookReview.objects.all().order_by('-created_at')
    #     paginator = PageNumberPagination()
    #     page = paginator.paginate_queryset(book_reviews , request)
    #     username = request.GET.get('username')
    #     if username:
    #         try:
    #             user = CustomUser.objects.get(username=username)
    #             page = book_reviews.filter(user=user)
    #         except:
    #             book_reviews = {
    #                 "message": "You sent invalid username with query params"
    #             }
    #             return Response(book_reviews , status=status.HTTP_400_BAD_REQUEST)
    #     serializer = BookReviewSerializer(page , many=True)
    #     return paginator.get_paginated_response(data=serializer.data)
    

    # def post(self , request):
    #     serializer = BookReviewSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

