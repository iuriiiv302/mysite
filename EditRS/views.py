from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response

from EditRS.serializers import UserSerializer


@api_view(["GET", ])
def get_users(request):
    users = User.objects.all().order_by('-date_joined')
    serializer = UserSerializer(users, many=True, context={'request': request})
    return Response(serializer.data)
