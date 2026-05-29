from .views import ImageTaskView
from django.urls import path

urlpatterns = [
    path('upload/', ImageTaskView.as_view(), name='image-upload'),
]