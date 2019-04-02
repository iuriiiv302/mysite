from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import University, Student, Author, Book, Shop

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')



class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = ('url', 'name')
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('url', 'first_name','last_name')
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('url', 'title', 'author')
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('url', 'first_name','last_name')
        fields = '__all__'
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('url', 'Name1', 'Adress', 'books')
        fields = '__all__'



