from django.conf.urls import url
from rest_framework import routers
from edit_shop_book.views import StudentViewSet, UniversityViewSet, AuthorViewSet, BookViewSet, ShopViewSet, BookUpdate, AuthorUpdate, ShopUpdate
from django.urls import path


router = routers.DefaultRouter()
router.register('students', StudentViewSet)
router.register('universities', UniversityViewSet)
router.register('Book', BookViewSet)
router.register('Author', AuthorViewSet)
router.register('Shop', ShopViewSet)

urlpatterns = [
path('Book/<int:pk>/', BookUpdate, name='book-update'),
path('A/<int:pk>/', AuthorUpdate, name='autor-update'),
path('Book/<int:pk>/', ShopUpdate, name='shop-update'),

]

urlpatterns = router.urls