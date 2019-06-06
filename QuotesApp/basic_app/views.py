from django.shortcuts import render
from django.views.generic import View,TemplateView
from basic_app.models import QuotePost
# Create your views here.
class IndexView(TemplateView):
    template_name = 'basic_app/index.html'
class QuoteListView(TemplateView):
    template_name = 'basic_app/quote_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quotes'] = QuotePost.objects.order_by('dateCreation')
        return context
