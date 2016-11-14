from django.shortcuts import render, redirect
from tables.media import Media
from django.contrib.auth.models import User
from django.conf import settings
from django.http import Http404
import PIL
import os
import uuid
from PIL import Image
from django.conf import settings
from tables.media import Media
from django.core.files import File
def image_resize(request):
    width = request.POST['width']
    height = request.POST['height']
    img =  request.POST['image']
    ext = img.split('.')[-1]
    if request.user.is_authenticated:
        username = request.user.username
        query = (Media.objects.filter(owner__username=username).filter(image=img) | Media.objects.filter(public=True)).first()
        if query is not None:
            imgpath = os.path.join(settings.MEDIA_ROOT,img)
            image = Image.open(imgpath)
            image = image.resize((width, height), PIL.Image.ANTIALIAS)
            filename = uuid.uuid4() + '.' + ext
            image.save(os.path.join(settings.MEDIA_ROOT,filename))
            reopen = open(os.path.join(settings.MEDIA_ROOT,filename),'r')
            django_file = File(reopen)
            media = Media()
            media.display_name = query.display_name + ' Resized'
            media.owner = query.owner
            media.public = query.public
            media.image.save(filename, django_file, save=True)
            return redirect('/dashboard')
        else:
            raise Http404
    else:
        return redirect('/login?next=/upload')