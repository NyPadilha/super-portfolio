from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Profile, Project, CertifyingInstitution, Certificate
from .serializers import (
    ProfileSerializer,
    ProjectSerializer,
    CertifyingInstitutionSerializer,
    CertificateSerializer,
)
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.
class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]

        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if self.request.method == "GET":
            profile_id = self.kwargs.get("pk")
            profile = Profile.objects.get(id=profile_id)

            return render(request, "profile_detail.html", {"profile": profile})

        return super().retrieve(request, *args, **kwargs)


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertifyingInstitutionViewSet(ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer
    permission_classes = [IsAuthenticated]


class CertificateViewSet(ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [IsAuthenticated]
