from django.shortcuts import render, redirect
from tables.media import Media
from django.contrib.auth.models import User
from django.conf import settings
from django.http import Http404, HttpResponse
from django.core.files.base import ContentFile
import uuid
from tables.api_management import APIManagement

def refresh_key(request):
    key = request.GET.get('key','')
    user = request.user
    if user.is_authenticated:
        api_management = APIManagement.objects.filter(key=key, developer__user=user).first()
        if api_management is None:
            raise Http404
        api_management.key = str(uuid.uuid4())
        api_management.save()
        return HttpResponse(status=200)
    else:
        raise Http404

def delete_key(request):
    key = request.GET.get('key','')
    user = request.user
    if user.is_authenticated:
        api_management = APIManagement.objects.filter(key=key, developer__user=user).first()
        if api_management is None:
            raise Http404
        api_management.delete()
        return HttpResponse(status=200)
    else:
        raise Http404