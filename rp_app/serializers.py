from rest_framework import serializers
from .models import ClientURL


class ClientURLSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientURL
        fields = "__all__"
        depth = 1
