
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   
    path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('chat/', views.chat, name='chat'),
    path('chat/api/', views.chat_api, name='chat_api'),
    path('logout/', views.custom_logout_view, name='logout'),
]

