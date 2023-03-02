from rest_framework import generics, permissions
from .serializers import ProjectSerializer
from portfolio.models import Project

class APIProjectsList(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.filter(dateProject__isnull=False).order_by('-dateProject')




