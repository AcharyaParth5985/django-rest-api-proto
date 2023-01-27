from django.shortcuts import render
from rest_framework import permissions as p
from django.contrib.auth import login, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.request import Request
from rest_framework.response import Response
from user import serializers as s
from user import models as m
from user.roles import Role

USER_SERIALIZER_MAP = {
    Role.ADMIN: s.BaseUserSerializer(m.Admin),
    Role.DEPT_OFFICER: s.BaseUserSerializer(m.DeptOfficer),
    Role.STUDENT: s.BaseUserSerializer(m.Student),
    Role.VOLUNTEER: s.BaseUserSerializer(m.Volunteer),
}

# Create your views here.
@api_view(["POST"])
def insert_user(req: Request):
    _role = req.data.get("role")
    if _role is None:
        return Response("Role is Not Supplied", status=400)

    serializer_class = USER_SERIALIZER_MAP.get(_role)
    if serializer_class is None:
        return Response("Invalid Role Supplied", status=400)

    serializer = serializer_class(data=req.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=400)
    serializer.save()

    return Response(status=200)


@api_view(["POST"])
def login_user(req: Request):
    srlzr = s.UserLoginSerializer(data=req.data)
    if not srlzr.is_valid():
        return Response(srlzr.errors, status=400)

    user = m.User.objects.filter(username=srlzr.validated_data["username"]).first()
    if user is None:
        return Response("User Not Found in System", status=404)

    if not user.check_password(srlzr.validated_data["password"]):
        return Response("Wrong password", status=401)

    login(req, user)
    return Response(status=200)


@api_view(["GET"])
@permission_classes([p.IsAuthenticated])
def logout_user(req: Request):
    logout(req)
    return Response(status=200)


@api_view(["POST"])
@permission_classes([p.IsAuthenticated])
def change_password(req: Request):
    serializer = s.UserChangePasswordSerialzer(data=req.data)

    if not serializer.is_valid():
        return Response(serializer.errors, status=400)

    if serializer.validated_data["password1"] != serializer.validated_data["password2"]:
        return Response("password do not match", status=400)

    req.user.set_password(serializer.validated_data["password1"])
    req.user.save()

    return Response(status=200)


@api_view(["GET"])
@permission_classes([p.IsAuthenticated])
def get_user(req: Request):
    return Response(req.user.get_username())
