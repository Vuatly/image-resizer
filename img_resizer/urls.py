from django.urls import path, reverse_lazy

from .models import Image
from .views import ImageListView, ImageCreateView, ImageDetailView

app_name = 'img_resizer'

urlpatterns = [
    path('', ImageListView.as_view(), name='img_list'),
    path('img_create/', ImageCreateView.as_view(
        success_url=reverse_lazy('img_resizer:img_list')), name='img_create'
    ),
    path('img_detail/<int:pk>/', ImageDetailView.as_view(), name='img_detail'),
]
