from django import forms
from django.shortcuts import get_object_or_404
from django.core.exceptions import ImproperlyConfigured

from core.models import ContentImage, Article


class ContentImageForm(forms.ModelForm):

    class Meta:
        model = ContentImage
        fields = ('image',)

    def __init__(self, *args, **kwargs):
        article_id = kwargs.pop('article_id', None)
        super().__init__(*args, **kwargs)

        self.article_id = article_id

    def clean(self):
        cleaned_data = super().clean()
        if not self.instance.id:
            # new image
            if self.article_id:
                article = get_object_or_404(Article, pk=self.article_id)
                self.instance.article = article
            else:
                raise ImproperlyConfigured("Expected kwarg 'article_id' "
                                           "cannot be none for create view.")
        return cleaned_data
