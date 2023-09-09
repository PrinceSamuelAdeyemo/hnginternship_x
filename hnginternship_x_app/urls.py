from django.urls import path
from .views import Index

urlpatterns = [
    path('<str:pk1>/<str:pk2>', Index.as_view(), name = 'stage1'),
]
