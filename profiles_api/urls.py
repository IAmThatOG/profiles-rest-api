from unicodedata import name
from webbrowser import get
from django.urls import path
from profiles_api.views import test_views, hello_views

urlpatterns = [
    path("test/", test_views.test_list),
    path("hello/", hello_views.HelloList.as_view())
    # path("test/", test_view.post, name="test_post"),
]
