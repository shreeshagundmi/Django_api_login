from django.urls import path
from . import views


urlpatterns = [
    path('std', views.std),
    path('list_view', views.list_view),
    path('detail_view/<id>', views.detail_view),
    path('update_view/<id>', views.update_view, name='student-edit'),
    path('<id>/delete', views.delete_view, name='student-delete')
]
