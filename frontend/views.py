from django.shortcuts import render, redirect

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
        # TODO Get Data
        return render(request, 'image.html', context={'a':123})
    else:
        return redirect('/login?next=/upload')
