from django.urls import path
from books import views

urlpatterns = [
    path('house/',views.fun1)
]