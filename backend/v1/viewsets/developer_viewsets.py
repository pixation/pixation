from django.http import *
from django.contrib.auth.models import User

from rest_framework import viewsets, filters
from rest_framework.response import Response

from backend.v1.serializers.developer_serializer import *
from tables.developer import Developer


class DeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    
    def create(self, serializer):
        if self.request.user.is_authenticated():
            if not Developer.objects.filter(user = self.request.user):
                serializer.save(user = self.request.user)
                print(serializer.data)
                return Response(serializer.data)
            else:
                raise serializers.ValidationError(
                    {
                        "Error": "User is already a developer",
                    }
                )
        else:
            raise serializers.ValidationError(
                {
                    "Error":"Unauthorized",
                }
            )
    
    