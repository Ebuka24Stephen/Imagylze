from .views import ImageTaskView, GetImage, DownloadImage
from django.urls import path

urlpatterns = [
    path('upload/', ImageTaskView.as_view(), name='image-upload'),
    path('upload/<int:task_id>/', GetImage.as_view(), name='image-get'),
    path('download/<int:task_id>/', DownloadImage.as_view(), name='image-download'),
]
