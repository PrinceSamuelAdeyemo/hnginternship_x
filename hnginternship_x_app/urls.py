from django.urls import path
from .views import Index

urlpatterns = [
    path('api', Index.as_view(), name = 'stage1'),
]
