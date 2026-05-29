# Imagylze

Imagylze is an asynchronous image processing API built with Django and Celery.  
It allows users to upload images (PNG/JPEG), apply transformations such as resizing, and retrieve processed results via a background task system.

## Features

- Image upload (PNG & JPEG only)
- Asynchronous processing using Celery
- Task-based system (PENDING → PROCESSING → COMPLETED)
- Image resizing with Pillow
- REST API built with Django REST Framework
- Media file storage system

## Architecture

Client → Django API → Database (Task Created) → Celery Worker → Pillow Processing → Media Storage → API Response

## API Endpoints

/api/uploads/

### Create Image Task
POST /api/image-tasks/

Form-data:
- image (file)
- width (int)
- height (int)

Response:
{
    "id": 20,
    "image": "/media/images/filename.png",
    "status": "PENDING",
    "height": 200,
    "width": 400
}
---

## Workflow

1. Upload image via API
2. Task is created (PENDING)
3. Celery processes image in background
4. Image is resized using Pillow
5. Output is saved in /media/processed/
6. Client fetches result via API

## Installation

### Clone repo
git clone https://github.com/Ebuka24Stephen/imagylze.git

cd imagylze

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py migrate

## Tech Stack

- Django
- Django REST Framework
- Celery
- Redis
- Pillow


## Notes

- Only PNG and JPEG images are supported
- Processing is asynchronous (Celery required)
- Redis must be running for task queue
