from celery import shared_task
from imagylze import settings
from .models import ImageTask
from django.shortcuts import get_object_or_404
from PIL import Image
import os
from django.conf import settings


@shared_task
def process_image(task_id):
    task =  ImageTask.objects.get(id=task_id)
    try:
        task.status = ImageTask.TaskStatus.PROCESSING
        task.save()
        img = Image.open(task.image.path)
        width = task.width
        height = task.height
        # Example processing: resizing the image
        img = img.resize((width, height))
        img = img.convert("RGB")


        output_dir = os.path.join(settings.MEDIA_ROOT, "processed")
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f"{task_id}.jpg")
        img.save(output_path)
        task.output_image = f"processed/{task_id}.jpg"
        task.status = ImageTask.TaskStatus.COMPLETED
        task.save()

        return task.output_image

    except Exception as e:
        task.status = ImageTask.TaskStatus.FAILED
        task.save()
        raise e