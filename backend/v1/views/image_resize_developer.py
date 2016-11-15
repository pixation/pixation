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
from django.conf import settings

from django.core.files import File
from django.http import JsonResponse
import numpy as np


from skimage import transform, util
import numpy as np
from skimage import filters, color

from tables.media import Media
from tables.api_management import APIManagement
from tables.developer import Developer


def image_resize2(request):
    height = int(request.GET.get('height',''))
    width = int(request.GET.get('width',''))
    img = request.GET.get('image','')
    ext = img.split('.')[-1]
    key = request.GET.get('key','')
    # print(key)
    print(height,width)
    # query = APIManagement.objects.filter(key=key).filter(developer__user__media__image=image)
    query = Media.objects.filter(image=img).filter(owner__developer__api_management__key=key).first()
    print(query,query.height,query.width)
    if query:
        imgpath = os.path.join(settings.MEDIA_ROOT,img)
        image = Image.open(imgpath)
        np_img= np.array(image)
        np_img = util.img_as_float(np_img)
        eimg = filters.sobel(color.rgb2gray(np_img))
        print('Before transform')
        out = transform.seam_carve(np_img, eimg, 'vertical', query.width - width)*255
        eimg = filters.sobel(color.rgb2gray(out))
        # out = transform.seam_carve(out, eimg, 'horizontal', query.height-height)*255
        out = out.astype(np.uint8)
        image = Image.fromarray(out)
        output = BytesIO()
        image.save(output,'BMP')
        filecontent = ContentFile(output.getvalue())
        media = Media()
        media.owner = query.owner
        media.dislay_name = img + ' Resized'
        media.public = query.public
        media.image.save('image.png',File(filecontent), save=True)
        response = HttpResponse(content_type="image/jpeg")
        image.save(response, "JPEG")
        return response