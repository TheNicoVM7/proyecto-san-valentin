from django.urls import path
from . import views

urlpatterns = [
    path('', views.propuesta, name='propuesta'),
    path('celebracion/', views.exito, name='exito'),
]