
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from .views import base_html

urlpatterns=[
    path('',base_html.as_view()),

] 