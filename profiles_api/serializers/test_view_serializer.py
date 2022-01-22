from unicodedata import name
from unittest.util import _MAX_LENGTH
from rest_framework import serializers


class TestViewSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)
