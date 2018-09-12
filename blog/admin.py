from django.contrib import admin
from blog.models import Blogcontent, Aboutme, Img

# Register your models here.
class BlogcontentAdmin(admin.ModelAdmin):
	list_display = ['title', 'text', 'owner', 'date_added']

class AboutmeAdmin(admin.ModelAdmin):
	list_display = ['text', 'owner', 'date_added']

class ImgAdmin(admin.ModelAdmin):
	list_display = ['pic', 'intro', 'owner', 'date_added']
		

admin.site.register(Blogcontent, BlogcontentAdmin)
admin.site.register(Aboutme, AboutmeAdmin)
admin.site.register(Img, ImgAdmin)