from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

# Create your views here.

from .forms import ProfileForm
from .models import UserProfile

# Create your views here.

class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {'form': form})

    def post(self, request):
        subbmited_form = ProfileForm(request.POST, request.FILES)
        if subbmited_form.is_valid():
            # store_file(request.FILES['image'])
            profile = UserProfile(image=request.FILES['user_image'])
            profile.save()
            return HttpResponseRedirect('/profiles') 

        return render(request, "profiles/create_profile.html", {'form': subbmited_form})