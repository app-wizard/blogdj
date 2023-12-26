from django.urls import path
from . import views as myblog_views

urlpatterns = [
    path('', myblog_views.index, name='index'),
]