from django.urls import path
from basic_app import views
app_name = 'basic_app'
urlpatterns = [
    path('quotes/', views.QuoteListView.as_view(), name='quotes'),
    path('quotes/<int:pk>/', views.QuoteDetailView.as_view(), name='detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),
    path('create/', views.QuoteCreateView.as_view(), name='create'),
    path('addAuthor/', views.AuthorCreateView.as_view(), name='add'),
    path('author_update/<int:pk>/', views.AuthorUpdateView.as_view(), name='quote_update'),
    path('author_delete/<int:pk>/', views.AuthorDeleteView.as_view(), name='quote_delete'),
    path('quote_update/<int:pk>/', views.QuoteUpdateView.as_view(), name='quote_update'),
    path('quote_delete/<int:pk>/', views.QuoteDeleteView.as_view(), name='quote_delete'),
]
