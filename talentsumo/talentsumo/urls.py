"""
URL configuration for talentsumo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create_note/', views.create_note, name='create_note'),
    path('view_note/<int:note_id>/', views.view_note, name='view_note'),
    path('edit_note/<int:note_id>/', views.edit_note, name='edit_note'),
    path('share_note/<int:note_id>/', views.share_note, name='share_note'),
    path('accounts/profile/', views.profile, name='profile'),
    path('view_all_notes/', views.view_all_notes, name='view_all_notes'),
]