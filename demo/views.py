from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from core.models import Article
from .forms import ContentImageForm


class ArticleListView(ListView):
    template_name = 'demo/article-list.html'
    model = Article
    # our model doesn't have default odering so apply ordering here
    ordering = ('-pk',)


class ContentImageCreateView(CreateView):
    template_name = 'demo/image-form.html'
    form_class = ContentImageForm
    success_url = reverse_lazy('article-list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['article_id'] = self.kwargs['article']
        return kwargs

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)