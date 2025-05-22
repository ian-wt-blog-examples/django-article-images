from django.views.generic import ListView

from core.models import Article


class ArticleListView(ListView):
    template_name = 'demo/article-list.html'
    model = Article
    # our model doesn't have default odering so apply ordering here
    ordering = ('-pk',)

