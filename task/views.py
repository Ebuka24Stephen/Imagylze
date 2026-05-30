from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ImageTask
from .serializers import ImageTaskSerializer
from .tasks import process_image
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from django.conf import settings 
from django.http import FileResponse
import os

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

class GetImage(APIView):
    def get (self, request, task_id):
        task = get_object_or_404(ImageTask, id=task_id)
        serializer = ImageTaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)


from django.http import FileResponse

class DownloadImage(APIView):
    def get(self, request, task_id):
        task = get_object_or_404(ImageTask, id=task_id)

        if not task.output_image:
            return Response(
                {"error": "Output image not found."},
                status=404
            )

        file_path = task.output_image.path
        if not os.path.exists(file_path):
            return Response(
                {"error": "File not found on server."},
                status=404
            )
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))