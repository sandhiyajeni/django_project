from django.urls import path
from page import views

urlpatterns = [
    path('home/',views.home),
    path('index/',views.index)
]