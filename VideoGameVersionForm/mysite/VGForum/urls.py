from django.urls import path
from . import views


app_name = 'VGForum'

urlpatterns = [
    path('', views.version_list, name='version_list'),
    path('version/<int:pk>/', views.version_detail, name='version_detail'),
    path('version/create/', views.vg_create, name='vg_create'),
    path('search/', views.post_search, name='post_search'),
]