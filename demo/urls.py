from django.urls import path

from .views import (
    ArticleListView,
    ContentImageCreateView,
    ContentImageUpdateView
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('add-image/<int:article>/', ContentImageCreateView.as_view(),
         name='create-image'),
    path('update-image/<int:image>/', ContentImageUpdateView.as_view(),
         name='update-image'),
]
