from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

from django.shortcuts import render
from django.views import View

from .forms import ProfileForm

# Create your views here.


def store_file(file):
    with open('temp/screenshot.jpg', 'wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)

class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {'form': form})

    def post(self, request):
        subbmited_form = ProfileForm(request.POST, request.FILES)
        if subbmited_form.is_valid():
            store_file(request.FILES['image'])
            return HttpResponseRedirect('/profiles') 

        return render(request, "profiles/create_profile.html", {'form': subbmited_form})