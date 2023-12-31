"""
URL configuration for project project.

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
from django.urls import path
from django.contrib import admin
from tasks import views

urlpatterns = [
    path('admin',admin.site.urls),
    path('', views.AuthView.as_view()),
    path('auth/', views.AuthView.as_view(), name='auth'),
    path('logout/', views.logout_view, name='logout'),
    path('cabinet/', views.TaskList.as_view(), name="cabinet"),
    path('new_task/', views.TaskCreate.as_view(), name='new_task'),
    path('<pk>/delete/',views.DeleteTaskView.as_view(), name='delete'),
    path('<pk>/update/',views.UpadateStatusView.as_view(), name='update')
]
