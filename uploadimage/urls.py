from django.urls import path
from .views import ImageUpload, ImageList, ImageDetail, ImageLink

urlpatterns = [
    path('images/', ImageList.as_view(), name='image-list'),
    path('images/upload/', ImageUpload.as_view(), name='image-upload'),
    path('images/<int:pk>/', ImageDetail.as_view(), name='image-detail'),
    path('images/<int:pk>/link/', ImageLink.as_view(), name='image-link'),
]