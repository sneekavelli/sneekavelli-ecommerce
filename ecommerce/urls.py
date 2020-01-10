"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from . import views
from .views import (
	home_page,
	exclusive_page,
    tracksuits_page,
    contact_page,
    login_page
	)

urlpatterns = [
    
    path('home/', home_page),
    path('contact/', contact_page),
    path('login/', login_page),
	path('exclusive/', exclusive_page),
    path('tracksuits/', tracksuits_page),
    path('admin/', admin.site.urls),
  
]
