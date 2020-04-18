from django.urls import path
from . import views

urlpatterns = [
    path('', views.avalible_oppurtunities, name='avalible_oppurtunities'),
]
