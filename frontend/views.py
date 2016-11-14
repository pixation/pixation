from django.shortcuts import render, redirect
from tables.media import Media
from django.contrib.auth.models import User
from django.conf import settings
from django.http import Http404

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated():
        return render(request, 'dashboard.html')
    else:
        return redirect('/login?next=/dashboard')

def upload(request):
    if request.user.is_authenticated():
        return render(request, 'upload.html')
    else:
        return redirect('/login?next=/upload')

def image(request, username, img):
    if request.user.is_authenticated():
        query = Media.objects.filter(owner__username=username).filter(image=img).first()
        if query is not None:
            if (request.user == query.owner) or (query.public == True):
                return render(request, 'image.html', context={'image': query.image.url, 'public': query.public, 'owner': query.owner.username})
        # Else All
        raise Http404
    else:
        return redirect('/login?next=/upload')
