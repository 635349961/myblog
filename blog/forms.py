from django import forms
from .models import Blogcontent, Aboutme, Img

class BlogcontentForm(forms.ModelForm):
	class Meta:
		model = Blogcontent
		fields = ['title', 'text']
		widgets = {'text': forms.Textarea(attrs={'cols':80})}
		labels = {'title': '标题', 'text': '内容'}
		
class AboutmeForm(forms.ModelForm):
	class Meta:
		model = Aboutme
		fields = ['text']
		labels = {'text': ''}

class ImgForm(forms.ModelForm):
	class Meta:
		model = Img
		fields = ['intro']
		labels = {'intro': '介绍'}