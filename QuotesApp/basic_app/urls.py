from django.urls import path
from basic_app import views
urlpatterns = [
    path('second/', views.second, name='second'),
]
