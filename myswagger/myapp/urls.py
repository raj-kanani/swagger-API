from django.urls import path
from . import views

urlpatterns = [
    path('API/', views.SwaggerAPI.as_view(), name='API'),
]
