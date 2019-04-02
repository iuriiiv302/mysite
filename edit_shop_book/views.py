from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from edit_shop_book.serializers import UserSerializer, GroupSerializer,BookSerializer,AuthorSerializer,ShopSerializer
from .models import University, Student,Author,Book,Shop
from .serializers import UniversitySerializer, StudentSerializer

from django.views.generic.edit import UpdateView


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class UniversityViewSet(viewsets.ModelViewSet):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class BookUpdate(UpdateView):
    model = Book
    fields = ['title']


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name']

class ShopUpdate(UpdateView):
    model = Shop
    fields = ['Name1']

