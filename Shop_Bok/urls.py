from django.urls import path
from . import views

urlpatterns = [
    path('bok/', views.bok_detail, name='bok_detail'),
    path('autor/', views.autor_detail, name='autor_detail'),
    path('shop/', views.shop_detail, name='shop_detail'),
    path('', views.shop_all, name='shop_all'),
    path('bok/<int:pk>/', views.bokinfo, name='bokinfo'),
    path('autor/<int:pk>/', views.Autorinfo, name='autorinfo'),
    path('shop/<int:pk>/', views.shopinfo, name='shopinfo'),
]
