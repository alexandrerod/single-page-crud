from django.urls import path
from .views import ListViews

app_name = 'example'


urlpatterns = [
    path('', ListViews.as_view(), name='index'),
]
