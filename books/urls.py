from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import BookListAPIView, book_api_view, BookDetailAPIView, BookDeleteAPIView, BookUpdateAPIView, \
    BookCreateAPIView, BookCreateListAPIView,BookUpdateDelete,BookViewset



app_name = 'books'

router=SimpleRouter()
router.register("books", BookViewset, basename="books")

urlpatterns = [
    # path('bookdestroyupdate/<int:id>/', BookUpdateDelete.as_view()),
    # path('bookcreatelist/<int:id>/', BookCreateListAPIView.as_view()),
    # path("books/", BookListAPIView.as_view()),
    # path("books/create/", BookCreateAPIView.as_view()),
    # path('books/<int:id>/', BookDetailAPIView.as_view()),
    # path('books/<int:id>/delete/', BookDeleteAPIView.as_view()),
    # path('books/<int:id>/update/',BookUpdateAPIView.as_view()),
    # path('books/', book_api_view),
]

urlpatterns = urlpatterns + router.urls