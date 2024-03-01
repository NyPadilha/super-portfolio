from rest_framework.serializers import ModelSerializer
from .models import Profile, Project, CertifyingInstitution, Certificate


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class CertificateSerializer(ModelSerializer):
    class Meta:
        model = Certificate
        fields = "__all__"


class CertifyingInstitutionSerializer(ModelSerializer):
    class Meta:
        model = CertifyingInstitution
        fields = "__all__"
