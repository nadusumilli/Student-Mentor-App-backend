from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from rest_framework_json_api.relations import *


#load django and webapp models
#from django.contrib.auth.models import *
from api.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups', 'password', 'student', 'mentor')
        #fields = ('url', 'username', 'email', 'groups', 'experiments')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission
        fields = ('name', 'codename')

class MentorSerializer(serializers.HyperlinkedModelSerializer):
    #fields = '__all__'
    user = UserSerializer(read_only=True)
    class Meta:
        model = Mentor
        fields = ('user', 'video', 'cv', 'bio', 'researchinterest', 'institution','job','fieldofstudy', 'webpage', 'experience', 'students')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Student
        fields = ('user', 'mentors', 'mentorsclicked','noofmentors')

# class EventSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Event
#         fields = ('title', 'description')

# class DegreeSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Degree
#         fields = ('title', 'description')