from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

app_name = "users"
urlpatterns = [
	path('changepassword/', views.changepassword, name='changepassword'),
	path('logout/', views.logout_view, name='logout'),
	path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
	path('register/', views.register, name="register"),
]