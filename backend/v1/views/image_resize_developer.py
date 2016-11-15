from django.shortcuts import render, redirect
from tables.media import Media
from django.contrib.auth.models import User
from django.conf import settings
from django.http import Http404, HttpResponse
from django.core.files.base import ContentFile
from io import BytesIO
import codecs
import PIL
import os
import uuid
import json
from PIL import Image
from urllib.parse import urlparse

from django.conf import settings

from django.core.files import File
from django.http import JsonResponse
import numpy as np
from datetime import datetime

from skimage import transform, util
import numpy as np
from skimage import filters, color

from tables.media import Media
from tables.api_management import APIManagement
from tables.developer import Developer
from tables.cached_media import CachedMedia

def image_resize2(request):
    height = int(request.GET.get('height',''))
    width = int(request.GET.get('width',''))
    img = request.GET.get('image','')
    ext = img.split('.')[-1]
    key = request.GET.get('key','')
    referer = request.META.get('HTTP_REFERER','')
    referer = urlparse(referer).hostname
    # referer = 'google.com'
    print(referer)
    # print(key)
    # query = APIManagement.objects.filter(key=key).filter(developer__user__media__image=image)
    query = Media.objects.filter(image=img).filter(owner__developer__api_management__key=key, owner__developer__api_management__sources__host=referer).first()
    if query is not None:
        api_management = APIManagement.objects.filter(key=key).first()
        if api_management.quota <= 0:
            imgpath = os.path.join("notallowed.png")
            image = Image.open(imgpath)
            response = HttpResponse(content_type="image/jpeg")
            image.save(response, "JPEG")
            return response
        else:
            api_management.quota -= 1
            api_management.save() 
        cache_query = CachedMedia.objects.filter(original=query).filter(height=height).filter(width=width).filter(api_type='1').first()
        if cache_query is not None:
            print("HIT")
            cache_query.last_hit_at = datetime.now()
            cache_query.save()
            print(cache_query.image)
            imgpath = os.path.join(settings.MEDIA_ROOT, str(cache_query.image))
            image = Image.open(imgpath)
            response = HttpResponse(content_type="image/jpeg")
            image.save(response, "JPEG")
            return response
        else:
            print(query.width,width,query.height,height)
            if query.width - width <0 or query.height -height <0:
                raise Http404
            imgpath = os.path.join(settings.MEDIA_ROOT,img)
            image = Image.open(imgpath)
            np_img= np.array(image)
            np_img = util.img_as_float(np_img)
            eimg = filters.sobel(color.rgb2gray(np_img))
            out = transform.seam_carve(np_img, eimg, 'horizontal', query.height - height)
            out = out/out.max()
            out = out*255
            eimg = filters.sobel(color.rgb2gray(out))
            out = transform.seam_carve(out, eimg, 'vertical', query.width - width)
            out = out/out.max()
            out = out*255
            out = out.astype(np.uint8)
            image = Image.fromarray(out)
            # image = image.resize((width, height), PIL.Image.ANTIALIAS)
            output = BytesIO()
            image.save(output,'JPEG')
            filecontent = ContentFile(output.getvalue())
            media = CachedMedia()
            media.owner = query.owner
            media.dislay_name = img + ' Resized'
            media.public = query.public
            media.api_type = '1'
            media.last_hit_at = datetime.now()
            media.original = query
            media.image.save('image.jpg',File(filecontent), save=True)
            response = HttpResponse(content_type="image/jpeg")
            image.save(response, "JPEG")
            return response
    else:
        imgpath = os.path.join("notallowed.png")
        image = Image.open(imgpath)
        response = HttpResponse(content_type="image/jpeg")
        image.save(response, "JPEG")
        return response