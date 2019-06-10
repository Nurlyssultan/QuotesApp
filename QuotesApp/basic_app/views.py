from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView
from basic_app.models import QuotePost,QuoteAuthor
# Create your views here.
class IndexView(TemplateView):
    template_name = 'basic_app/index.html'
class QuoteListView(ListView):
    context_object_name = 'quotes'
    model = QuotePost
    template_name = 'basic_app/quote_list.html'
class QuoteDetailView(DetailView):
    context_object_name = 'quote_detail'
    model = QuotePost
    template_name = 'basic_app/quote_detail.html'
class AuthorListView(ListView):
    context_object_name = 'authors'
    model = QuoteAuthor
    template_name = 'basic_app/author_list.html'
class AuthorDetailView(DetailView):
    context_object_name = 'author_detail'
    model = QuoteAuthor
    template_name = 'basic_app/author_quotes.html'
