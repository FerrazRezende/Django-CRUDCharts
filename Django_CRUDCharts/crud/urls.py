from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('read', views.view, name='read'),

    #actions
    path('delete/<int:pk>', views.delete, name='delete'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('read/<int:pk>', views.read, name='read')
]