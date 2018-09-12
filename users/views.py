from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from .forms import ChangepwdForm

# Create your views here.
def changepassword(request):
	if request.method != "POST":
		form = ChangepwdForm()
	else:
		form = ChangepwdForm(data=request.POST)
		if form.is_valid():
			username = request.user.username
			oldpassword = request.POST.get('oldpassword', '')
			user = authenticate(username=username, password=oldpassword)
			if user is not None and user.is_active:
				newpassword = request.POST.get('newpassword1', '')
				user.set_password(newpassword)
				user.save()
				login(request, user)
				return HttpResponseRedirect(reverse('blog:mainpage'))
	context = {'form': form}
	return render(request, 'users/changepassword.html', context)

def logout_view(request):
	logout(request)
	return HttpResponseRedirect(reverse('blog:mainpage'))


def register(request):
	if request.method != "POST":
		form = UserCreationForm()
	else:
		form = UserCreationForm(data=request.POST)

		if form.is_valid():
			new_user = form.save()
			authenticated_user = authenticate(username=new_user.username,password=request.POST['password1'])
			login(request,authenticated_user)
			return HttpResponseRedirect(reverse('blog:mainpage'))
	context = {'form': form}
	return render(request, 'users/register.html', context)

