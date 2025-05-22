from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from core.models import Article, ContentImage
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
    form_title = 'Create Image'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['article_id'] = self.kwargs.get('article', None)
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_title'] = self.form_title
        return context


# noinspection PyAttributeOutsideInit
class ContentImageUpdateView(ContentImageCreateView):
    model = ContentImage
    pk_url_kwarg = 'image'

    # override get/post to retrieve object (otherwise set to none)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return self.render_to_response(self.get_context_data())

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        return self.form_invalid(form)
