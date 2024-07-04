from django.shortcuts import render
from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet

from .models import Book
from .serializers import BookSerializer
from rest_framework.decorators import api_view
from rest_framework import generics, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


#
# class BookListAPIView(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#


class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True).data
        data = {
            "status": f"Returned {len(books)} books",
            "books": serializer
        }

        return Response(data)


# class BookDetailAPIView(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#     lookup_field = 'id'

class BookDetailAPIView(APIView):

    def get(self, request, id):
        try:
            book = Book.objects.get(id=id)

            serializer_data = BookSerializer(book).data

            data = {
                "status_code": "Successfully",
                "book": serializer_data
            }
            return Response(data)
        except Exception:
            return Response(
                {
                    "status": False,
                    "message": "Book is not found"
                }, status=status.HTTP_404_NOT_FOUND
            )


# class BookDeleteAPIView(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#     lookup_field = 'id'


class BookDeleteAPIView(APIView):
    def delete(self, request, id):
        try:
            book = Book.objects.get(id=id)
            book.delete()
            return Response(
                {
                    "status": True,
                    "message": "Successfully deleted"
                }, status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {
                    "status": False,
                    "message": "Delete doesnot exists"
                }, status=status.HTTP_400_BAD_REQUEST
            )


# class BookUpdateAPIView(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#     lookup_field = "id"


class BookUpdateAPIView(APIView):
    def put(self, request, id):
        book = get_object_or_404(Book.objects.all(), id=id)
        data = request.data
        serializer = BookSerializer(instance=book, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            saved = serializer.save()
        return Response({
            "status": True,
            "book": f" Book{saved} successfully updated"
        })


# class BookCreateAPIView(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializers
#     lookup_field = 'id'


class BookCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)
        if serializer.is_valid():
            datas=serializer.save()
            response_data = {
                "status": "books are created to the database",
                "books": datas
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookCreateListAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'


class BookUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'




class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "id"













# Function based on the DRF

@api_view(['GET'])
def book_api_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)
