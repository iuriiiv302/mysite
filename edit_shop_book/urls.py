from django.conf.urls import url
from rest_framework import routers
from edit_shop_book.views import StudentViewSet, UniversityViewSet,AuthorViewSet,BookViewSet,ShopViewSet,BookUpdate
from django.urls import path


router = routers.DefaultRouter()
router.register('students', StudentViewSet)
router.register('universities', UniversityViewSet)
router.register('Book', BookViewSet)
router.register('Author', AuthorViewSet)
router.register('Shop', ShopViewSet)

urlpatterns = [
path('book/<int:pk>/', BookUpdate, name='book-update'),
]

urlpatterns = router.urls