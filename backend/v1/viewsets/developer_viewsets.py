from django.http import *
from django.contrib.auth.models import User

from rest_framework import viewsets, filters
from rest_framework.response import Response

from backend.v1.serializers.developer_serializer import *
from tables.developer import Developer
from tables.api_management import APIManagement
from tables.source import Source
import uuid

class MakeDeveloperViewSet(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    http_method_names = ['get','post','delete']
    def perform_create(self, serializer):
        if self.request.user.is_authenticated():
            if not Developer.objects.filter(user = self.request.user):
                serializer.save(user = self.request.user)
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

class APIManagementViewSet(viewsets.ModelViewSet):
    queryset = APIManagement.objects.all()
    serializer_class = APIManagementSerializer
    http_method_names = ['get','post','delete']
    
    def perform_create(self, serializer):
        if self.request.user.is_authenticated():
            query = Developer.objects.filter(user = self.request.user)
            if query:
                serializer.save(
                    developer=query[0],
                    key=uuid.uuid4(),
                    quota=1000
                    )
                print(serializer.data)
                return Response(serializer.data)
            else:
                raise serializers.ValidationError(
                    {
                        "Error":"Not a Developer"
                    }
                )
        else:
            raise serializers.ValidationError(
                {
                    "Error":"Unauthorized",
                }
            )

