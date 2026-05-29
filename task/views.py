from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ImageTask
from .serializers import ImageTaskSerializer
from .tasks import process_image
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

class ImageTaskView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = ImageTaskSerializer(data=request.data)
        if serializer.is_valid():
            task = serializer.save()
            # Trigger the Celery task
            process_image.delay(task.id)            

            return Response(
                ImageTaskSerializer(task).data,
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
