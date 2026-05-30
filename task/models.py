from django.db import models
from django.core.exceptions import ValidationError
import os

def image_format_validator(file):
    ext = os.path.splitext(file.name)[1].lower()
    valid_extensions = [".png", ".jpg", ".jpeg"]
    if ext not in valid_extensions:

        raise ValidationError("Only PNG and JPEG images are allowed.")

class ImageTask(models.Model):
    class TaskStatus(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        PROCESSING = 'PROCESSING', 'Processing'
        COMPLETED = 'COMPLETED', 'Completed'
        FAILED = 'FAILED', 'Failed'
    image = models.ImageField(upload_to='images/', validators=[image_format_validator])
    status = models.CharField(max_length=20, choices=TaskStatus.choices, default=TaskStatus.PENDING)
    height = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    output_image = models.ImageField(upload_to='output_images/', null=True, blank=True)