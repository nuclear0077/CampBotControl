from rest_framework import serializers

from CampAdmin.models import Users, TypeEducation, Faculties, Profile, Data


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('user_id', 'first_name', 'last_name', 'age', 'gender', 'city', 'is_active', 'department', 'admin')


class TypeEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeEducation
        fields = ('id', 'name',)


class FacultiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faculties
        fields = ('id', 'name',)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'name',)


class DataSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='descriptions')
    class Meta:
        model = Data
        fields = ('id', 'name')
