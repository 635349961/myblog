from django import forms
from django.db import models


class ChangepwdForm(forms.Form):
	oldpassword = forms.CharField(required=True, label="原密码", error_messages={'required':"请输入原密码",}, 
		widget=forms.PasswordInput(attrs={'placeholder':'原密码', 'rows':1,}) )
	newpassword1 = forms.CharField(required=True, label="新密码", error_messages={'required':"请输入新密码",}, 
		widget=forms.PasswordInput(attrs={'placeholder':'新密码', 'rows':1,}) )
	newpassword2 = forms.CharField(required=True, label="确认密码", error_messages={'required':"请再次输入新密码",}, 
		widget=forms.PasswordInput(attrs={'placeholder':'确认密码', 'rows':1,}) )
		
	def clean(self):
		if not self.is_valid():
			raise forms.ValidationError('所有项都为必填项')
		elif self.cleaned_data['newpassword1'] != self.cleaned_data['newpassword2']:
			raise forms.ValidationError('两次输入的密码不一样')
		else:
			cleaned_data = super().clean()

		return cleaned_data