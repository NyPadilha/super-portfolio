from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Profile, Project
from .serializers import ProfileSerializer, ProjectSerializer


# Create your views here.
class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
