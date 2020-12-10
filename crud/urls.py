"""crud URL Configuration

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
from students import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),
    path('esearch', include('esearch.urls')),
    path('emp/', include('employee.urls')),
    path('stud_list', views.studentsList, name="Stud-list"),
    path('stud_detail/<str:pk>/', views.studentsDetail, name="Stud-detail"),
    path('stud_add', views.studentsAdd, name="Stud-add"),
    path('stud_update/<str:pk>/', views.studentsUpdate, name="Stud-update"),
    path('stud_delete/<str:pk>/', views.studentsDelete, name="Stud-delete"),
    path('cars/', include('search.urls', namespace='cars')),
]

