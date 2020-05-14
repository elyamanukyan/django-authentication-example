# config/urls.py
from django.contrib import admin
from django.urls import path, include

from account.views import (
    home_screen_view,
    registration_view,
    logout_view,
    login_view,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_screen_view, name='home'),
    path('logout', logout_view, name='logout'),
    path('login', login_view, name='login'),
    path('register', registration_view, name='register'),
]
