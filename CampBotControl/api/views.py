from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from api.serializers import UsersSerializer, TypeEducationSerializer, FacultiesSerializer, ProfileSerializer, DataSerializer
from CampAdmin.models import TypeEducation, Users, Faculties, Data, Profile


class TypeEducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TypeEducation.objects.all()
    serializer_class = TypeEducationSerializer


class FacultiesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Faculties.objects.all()
    serializer_class = FacultiesSerializer

    def get_queryset(self):
        faculties = Data.objects.filter(
            type_education=self.kwargs.get('type_pk')
            )
        faculties = [fac.faculties for fac in faculties]
        return faculties


class ProfileEducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        profiles = Data.objects.filter(
            type_education=self.kwargs.get('type_pk'),
            faculties=self.kwargs.get('facultie_pk')
            )
        profiles = [prof.profile for prof in profiles]
        return profiles


class DataViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def get_queryset(self):
        description = Data.objects.filter(
            type_education=self.kwargs.get('type_pk'),
            faculties=self.kwargs.get('facultie_pk'),
            profile=self.kwargs.get('profile_pk'),
            )
        return description


class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def get_object(self):
        user = get_object_or_404(Users, user_id=self.kwargs.get('pk'))
        return user
