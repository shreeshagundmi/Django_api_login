from django.urls import path
from . import views


urlpatterns = [
    path('view', views.emp_view)
]
