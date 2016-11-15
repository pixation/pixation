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
from django.http import JsonResponse
import numpy as np


from skimage import transform, util
import numpy as np
from skimage import filters, color


def image_resize(request):
    json_data= json.loads(request.body.decode('utf-8'))
    width = abs(json_data['width'])
    height = abs(json_data['height'])
    img =  json_data['image']
    ext = img.split('.')[-1]
    if request.user.is_authenticated:
        username = request.user.username
        query = (Media.objects.filter(owner__username=username).filter(image=img) | Media.objects.filter(public=True)).first()
        if query.width - width <0 or query.height -height <0:
            return JsonResponse({
                "error":"Invalid height and width"
            })
        if query is not None:
            imgpath = os.path.join(settings.MEDIA_ROOT,img)
            image = Image.open(imgpath)
            np_img= np.array(image)
            np_img = util.img_as_float(np_img)
            eimg = filters.sobel(color.rgb2gray(np_img))
            out = transform.seam_carve(np_img, eimg, 'horizontal', query.height-height)*255
            eimg = filters.sobel(color.rgb2gray(out))
            out = transform.seam_carve(out, eimg, 'vertical', query.width-width)*255
            out = out.astype(np.uint8)
            image = Image.fromarray(out)
            # image = image.resize((width, height), PIL.Image.ANTIALIAS)
            output = BytesIO()
            image.save(output,'BMP')
            filecontent = ContentFile(output.getvalue())
            media = Media()
            media.owner = request.user
            media.dislay_name = query.display_name + ' Resized'
            media.public = query.public
            media.image.save('image.jpg',File(filecontent), save=True)
            return JsonResponse({
                'link':media.get_link()
                })
        else:
            raise Http404
    else:
        return redirect('/login?next=/upload')

