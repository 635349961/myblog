from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'
urlpatterns = [
	path('', views.mainpage, name='mainpage'),
	path('index', views.index, name='index'),
	path('show_picture', views.show_picture, name='show_picture'),
	path('aboutme', views.aboutme, name='aboutme'),
	path('writeblog', views.writeblog, name='writeblog'),
	path('blog/<int:blog_id>', views.blog, name='blog'),
	path('aboutme', views.aboutme, name='aboutme'),
	path('edit_aboutme', views.edit_aboutme, name='edit_aboutme'),
	path('uploadimg', views.uploadimg, name='uploadimg'),
	path('delblog/<int:blog_id>', views.delblog, name='delblog'),
	path('delpic/<int:item_id>', views.delpic, name='delpic'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)