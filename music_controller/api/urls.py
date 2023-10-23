from django.urls import path

from . import views

urlpatterns = [
    # url for the api (RoomView)
    path('rooms', views.RoomView.as_view()),
]