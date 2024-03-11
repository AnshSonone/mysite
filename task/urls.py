from django.urls import path
from . import views

urlpatterns = [
    path("video/", views.video, name="video"),
    path("", views.flights, name="flights"),
    path("upload/", views.upload, name="upload"),
    # path('update-flight/<str:pk>/', views.updateFlight, name='update-flight')
]