
from celery import shared_task
from django.conf import settings
from django.core.files import File

import task
from .models import ImageTask
from PIL import Image
import os


@shared_task
def process_image(task_id):
    task = ImageTask.objects.filter(id=task_id).first()
    if not task:
        return "Task not found"

    try:
        task.status = ImageTask.TaskStatus.PROCESSING
        task.save()

        img = Image.open(task.image.path)

        width = task.width or 300
        height = task.height or 300

        img = img.resize((width, height))
        img = img.convert("RGB")

        output_dir = os.path.join(settings.MEDIA_ROOT, "processed")
        os.makedirs(output_dir, exist_ok=True)

        output_path = os.path.join(output_dir, f"{task_id}.jpg")
        img.save(output_path)

        with open(output_path, "rb") as f:
            task.output_image.save(
                f"{task_id}.jpg",
                File(f),
                save=True
            )

        task.status = ImageTask.TaskStatus.COMPLETED
        task.save()

    except Exception as e:
        task.status = ImageTask.TaskStatus.FAILED
        task.save()
        raise e