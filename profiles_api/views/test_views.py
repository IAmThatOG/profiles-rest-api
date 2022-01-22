from webbrowser import get
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from profiles_api.serializers.test_view_serializer import TestViewSerializer
from profiles_core.dtos.response import BaseResponse


# Create your views here.
@api_view(["GET", "POST"])
def test_list(request, format=None):
    print(f"request: {request}")
    if request.method == "GET":
        an_apiview = [
            "Uses http methods as functions (get, post, patch put, delete)",
            "Is similar to django view",
            "is mapped manually to urls",
        ]
        return Response(
            data={"message": "Hello", "data": an_apiview}, status=status.HTTP_200_OK
        )
    if request.method == "POST":
        serializer = TestViewSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response(
                data=BaseResponse(
                    is_success=True,
                    message="Success",
                    status_code=status.HTTP_200_OK,
                    payload={"message": message},
                ).JSON
            )
        else:
            response = BaseResponse(
                is_success=True,
                message="Success",
                status_code=status.HTTP_400_BAD_REQUEST,
                payload=serializer.errors,
            )
            return Response(data=response.JSON, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
