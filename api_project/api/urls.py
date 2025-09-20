from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet

# create a router and register the BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),       # existing ListAPIView
    path('', include(router.urls)),                             # router-generated routes
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  # token endpoint
]
