from django.urls import path
from . import views

urlpatterns = [
    path('shop/all/bok/', views.bok_detail, name='bok_detail'),
    path('shop/all/autor/', views.autor_detail, name='autor_detail'),
    path('shop/all/shop/', views.shop_detail, name='shop_detail'),
    path('', views.shop_all, name='shop_all'),
    path('shop/all/bok/<int:pk>/', views.bokinfo, name='bokinfo'),
    path('shop/all/autor/<int:pk>/', views.Autorinfo, name='autorinfo'),
    path('shop/all/shop/<int:pk>/', views.shopinfo, name='shopinfo'),

]
