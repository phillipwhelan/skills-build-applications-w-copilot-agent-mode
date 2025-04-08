"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.api_root, name='api-root'),
    path('api/users/', views.users, name='users'),
    path('api/teams/', views.teams, name='teams'),
    path('api/activities/', views.activities, name='activities'),
    path('api/leaderboard/', views.leaderboard, name='leaderboard'),
    path('api/workouts/', views.workouts, name='workouts'),
]
