from rest_framework import serializers 
from .models import ImageTask 


class ImageTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageTask
        fields = "__all__"