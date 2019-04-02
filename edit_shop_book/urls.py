from django.conf.urls import url
from rest_framework import routers
from edit_shop_book.views import StudentViewSet, UniversityViewSet

router = routers.DefaultRouter()
router.register('students/', StudentViewSet)
router.register('universities/', UniversityViewSet)

urlpatterns = router.urls