from django.urls import path

from . import views

app_name = 'example'


urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.list_equipaments, name='list'),
    path('create/', views.create_equipaments, name='create'),
    path('update/<int:id>/', views.update_equipaments, name='update'),
]
