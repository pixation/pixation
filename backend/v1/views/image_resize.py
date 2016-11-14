from django.shortcuts import render, redirect
from tables.media import Media
from django.contrib.auth.models import User
from django.conf import settings
from django.http import Http404
from django.core.files.base import ContentFile
from io import BytesIO
import codecs
import PIL
import os
import uuid
import json
from PIL import Image
from django.conf import settings
from tables.media import Media
from django.core.files import File

def image_resize(request):
    json_data= json.loads(request.body.decode('utf-8'))
    width = json_data['width']
    height = json_data['height']
    img =  json_data['image']
    ext = img.split('.')[-1]
    if request.user.is_authenticated:
        username = request.user.username
        query = (Media.objects.filter(owner__username=username).filter(image=img) | Media.objects.filter(public=True)).first()
        if query is not None:
            imgpath = os.path.join(settings.MEDIA_ROOT,img)
            image = Image.open(imgpath)
            image = image.resize((width, height), PIL.Image.ANTIALIAS)
            output = BytesIO()
            image.save(output,'BMP')
            filecontent = ContentFile(output.getvalue())
            media = Media()
            media.owner = request.user
            media.dislay_name = img + ' Resized'
            media.public = query.public
            media.image.save('image.png',File(filecontent), save=True)
            return redirect(media.get_link())
        else:
            raise Http404
    else:
        return redirect('/login?next=/upload')