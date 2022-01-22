from django.urls import path
from profiles_api.views import test_view

urlpatterns = [
    path("hello/", test_view.HelloApiView.as_view()),
]
