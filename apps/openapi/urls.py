from django.urls import include, path
from rest_framework import routers

from apps.openapi import views

# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)
urlpatterns = [
    path('create_link_token', views.CreateLinkToken.as_view()),
]
