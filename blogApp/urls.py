from django.urls import path
from . import views


urlpatterns = \
    [
        # only need one path since i can inject html from a different file
        path('', views.index , name = 'index'),
    ]