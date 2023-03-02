from rest_framework import serializers
from portfolio.models import Project

class ProjectSerializer(serializers.ModelSerializer):
    dateProject = serializers.ReadOnlyField()

    class Meta:
        model = Project
        fields = ['id','title','description','url','dateProject','youtubeResourceID','image']

