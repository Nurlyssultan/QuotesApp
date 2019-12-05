from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from basic_app.models import QuotePost,QuoteAuthor
from django.urls import reverse_lazy
# Create your views here.
class IndexView(TemplateView):
    template_name = 'basic_app/index.html'
class QuoteListView(ListView):
    context_object_name = 'quotes'
    model = QuotePost
    template_name = 'basic_app/quote_list.html'
    paginate_by = 6
class QuoteDetailView(DetailView):
    context_object_name = 'quote_detail'
    model = QuotePost
    template_name = 'basic_app/quote_detail.html'
class QuoteCreateView(CreateView):
    context_object_name = 'quotes'
    fields = ('quoteDesription','quoteAuthor')
    model = QuotePost
    success_url = reverse_lazy("basic_app:detail")
class QuoteUpdateView(UpdateView):
    context_object_name = 'quote_detail'
    fields = ('quoteDesription','quoteAuthor')
    model = QuotePost
    success_url = reverse_lazy("basic_app:quotes")
class QuoteDeleteView(DeleteView):
    context_object_name = 'quote_detail'
    model = QuotePost
    success_url = reverse_lazy("basic_app:quotes")
class AuthorListView(ListView):
    context_object_name = 'authors'
    model = QuoteAuthor
    template_name = 'basic_app/author_list.html'
class AuthorDetailView(DetailView):
    context_object_name = 'author_detail'
    model = QuoteAuthor
    template_name = 'basic_app/author_detail.html'
class AuthorCreateView(CreateView):
    fields = ('author','famousFor','lifeRange')
    model = QuoteAuthor
    success_url = reverse_lazy("basic_app:authors")
class AuthorUpdateView(UpdateView):
    fields = ('author','famousFor','lifeRange')
    model = QuoteAuthor
    success_url = reverse_lazy("basic_app:authors")
class AuthorDeleteView(DeleteView):
    model = QuoteAuthor
    success_url = reverse_lazy("basic_app:authors")
