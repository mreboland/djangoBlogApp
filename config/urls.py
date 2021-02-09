"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

urlpatterns = [
    path('admin/', admin.site.urls),
    # Adding out login and out pages at the accounts/ URL
    path("accounts/", include("django.contrib.auth.urls")),
    # We add the account creation urls under the above because django reads top to bottom. We want the request to accounts/signup url to happen after django first looks in auth (above), and when it cannot find an auth proceed to the accounts app. Aka, check for user, if not create an account.
    path("accounts/", include("accounts.urls")),
    # Empty string indicates that URL requests should be redirected as is to blog's URLs for further instructions.
    path("", include("blog.urls")),
]
