from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def changepassword(request):
	return render(request, 'users/changepassword.html')

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
	content = {'form': form}
	return render(request, 'users/register.html', content)

