from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import register_view
from .views import profile_view
urlpatterns = [
    path('login/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),

]