from django.shortcuts import render, get_object_or_404
from blog.models import Blogcontent, Aboutme, Img
from .forms import BlogcontentForm, AboutmeForm, ImgForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models.base import ObjectDoesNotExist

# Create your views here.
def mainpage(request):
	newblog = Blogcontent.objects.order_by('-date_added')	
	context = {'newblog': newblog}
	return render(request, 'blog/mainpage.html', context)


def index(request):
	blogs = Blogcontent.objects.all().order_by('-date_added')
	context = {'blogs': blogs}
	return render(request, 'blog/index.html', context)

def blog(request,blog_id):
	blog = get_object_or_404(Blogcontent,id=blog_id)
	context = {'blog': blog}
	return render(request, 'blog/blog.html', context)

def show_picture(request):
	imgs = Img.objects.all()
	context = {'imgs': imgs}
	return render(request, 'blog/show_picture.html', context)

@login_required
def uploadimg(request):
	if request.method != 'POST':
		form = ImgForm()
	else:
		form = ImgForm(data=request.POST)
		if form.is_valid():
			new_img = Img(pic=request.FILES.get('pic'))
			new_img.owner = request.user
			new_img.intro = request.POST.get('intro','暂时没有介绍')
			new_img.save()

			return HttpResponseRedirect(reverse('blog:show_picture'))
	context = {'form': form}
	return render(request, 'blog/uploadimg.html', context)

@login_required
def aboutme(request):
	aboutmes = Aboutme.objects.filter(owner=request.user).order_by('-date_added')
	context = {'aboutmes': aboutmes}
	return render(request, 'blog/aboutme.html', context)

@login_required
def edit_aboutme(request):
	if request.method != 'POST':
		try:
			aboutme = Aboutme.objects.get(owner=request.user)
		except ObjectDoesNotExist:
			form = AboutmeForm()
		else:
			form = AboutmeForm(instance=aboutme)
	else:
		try:
			aboutme = Aboutme.objects.get(owner=request.user)
		except ObjectDoesNotExist:
			form = AboutmeForm(data=request.POST)
			if form.is_valid:
				new_aboutme = form.save(commit=False)
				new_aboutme.owner = request.user
				new_aboutme.save()
			return HttpResponseRedirect(reverse('blog:aboutme'))
		else:
			form = AboutmeForm(instance=aboutme,data=request.POST)
			if form.is_valid():
				form.save()
			return HttpResponseRedirect(reverse('blog:aboutme'))
	context = {'form': form}
	return render(request, 'blog/edit_aboutme.html', context)

@login_required
def writeblog(request):
	if request.method != 'POST':
		form = BlogcontentForm()
	else:
		form = BlogcontentForm(data=request.POST)
		if form.is_valid():
			new_form = form.save(commit=False)
			new_form.owner = request.user
			new_form.save()
			return HttpResponseRedirect(reverse('blog:index'))
	context = {'form': form}
	return render(request, 'blog/writeblog.html', context)

def delblog(request,blog_id):
	del_blog = Blogcontent.objects.get(id=blog_id)
	if del_blog.owner != request.user:
		return render(request, 'blog/nodel.html')
	else:
		del_blog.delete()
		return HttpResponseRedirect(reverse('blog:index'))

def delpic(request,item_id):
	del_pic = Img.objects.get(id=item_id)
	if del_pic.owner != request.user:
		return render(request, 'blog/nodel.html')
	else:
		del_pic.delete()
		return HttpResponseRedirect(reverse('blog:show_picture'))