from rest_framework.decorators import api_view
from rest_framework import permissions,status
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer

@api_view(["GET"])
def get_all_users(req):
    data = User.objects.all()
    serializer = UserSerializer(data,many=True)
    return Response(serializer.data)

@api_view(["POST"])
def insert_user(req):
    user = UserSerializer(data=req.data)
    if not user.is_valid():
        return Response(user.errors,status=status.HTTP_400_BAD_REQUEST)

    user.save()
    return Response(status=status.HTTP_200_OK)