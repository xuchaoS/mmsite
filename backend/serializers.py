"""
File Name: serializers
Author: shangxc
Created Time: 2019-06-30 18:28
"""
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from .models import Port


# Create your views here.

# Serializers define the API representation.
class PortSerializer(serializers.ModelSerializer):
    # time = serializers.DateTimeField('%Y-%m-%d %H:%M:%S', read_only=True)
    owner_name = serializers.CharField(source='owner.username', read_only=True)

    class Meta:
        model = Port
        fields = ('id', 'port', 'owner_name', 'owner')


if __name__ == '__main__':
    pass
