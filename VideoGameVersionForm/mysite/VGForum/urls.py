from django.urls import path
from . import views


app_name = 'VGForum'

urlpatterns = [
    path('', views.version_list, name='version_list'),
    path('version/<int:pk>/', views.version_detail, name='version_detail'),
]