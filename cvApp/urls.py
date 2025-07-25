"""
URL configuration for cvApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from .views import landing_view,analyze_view,login_view, register_view, logout_view,dashboard_view,edit_resume_view,suggestion_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', landing_view, name='home'),
    path('analyze/', analyze_view, name='analyze'),
    path('edit-resume/', edit_resume_view, name='edit_resume'),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('suggestions/', suggestion_view, name='suggestions'),
]
