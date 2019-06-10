from django.urls import path
from basic_app import views
urlpatterns = [
    path('quotes/', views.QuoteListView.as_view(), name='quotes'),
    path('quotes/<int:pk>/', views.QuoteDetailView.as_view(), name='detail'),
]
