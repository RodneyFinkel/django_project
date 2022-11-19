from rest_framework import serializers
from saas_app.models import Project, Tag
from users.models import Profile

#this class serializes the Project model so that it can be returned as JSON

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer(many=False)
    tags = TagSerializer(many=True)
    class Meta:
        model = Project
        fields = '__all__'
