from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    def get(self, request, format=None):
        an_apiview = [
            "Uses http methods as functions (get, post, patch put, delete)",
            "Is similar to django view",
            "is mapped manually to urls",
        ]
        return Response(data={"message": "Hello", "data": an_apiview}, status=200)
