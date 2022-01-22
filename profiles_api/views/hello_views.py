from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api.serializers.test_view_serializer import TestViewSerializer
from profiles_core.dtos.response import BaseResponse


class HelloList(APIView):
    def get(self, request, format=None):
        an_apiview = [
            "Uses http methods as functions (get, post, patch put, delete)",
            "Is similar to django view",
            "is mapped manually to urls",
        ]
        return Response(
            data={"message": "Hello", "data": an_apiview}, status=status.HTTP_200_OK
        )

    def post(self, request, format=None):
        serializer = TestViewSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Hello {name}"
            return Response(
                BaseResponse(
                    is_success=True,
                    message="Success",
                    status_code=status.HTTP_200_OK,
                    payload={"message": message},
                ).JSON,
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                data=BaseResponse(
                    is_success=True,
                    message="Failure",
                    status_code=status.HTTP_400_BAD_REQUEST,
                    payload=serializer.errors,
                ).JSON,
                status=status.HTTP_400_BAD_REQUEST,
            )
