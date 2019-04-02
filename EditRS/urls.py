from django.urls import path
from . import views
from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from EditRS.views import UserList, UserDetail, GroupList, GroupDetail

urlpatterns = patterns(
    path('users/', views.UserList, name='user-list'),
    path('users/<int:pk>/', views.UserDetail, name='user-detail'),
    path('groups/', views.GroupList, name='group-list'),
    path('groups/<int:pk>/', views.GroupDetail, name = 'group-detail')

)

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])

# Default login/logout views
urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)