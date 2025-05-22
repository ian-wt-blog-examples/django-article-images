from django.urls import path

from .views import (
    ArticleListView,
    ContentImageCreateView,
    ContentImageUpdateView,
    ContentImageListView
)

urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:article>/add-image/', ContentImageCreateView.as_view(),
         name='create-image'),
    path('update-image/<int:image>/', ContentImageUpdateView.as_view(),
         name='update-image'),
    path('<int:article>/images/', ContentImageListView.as_view(),
         name='image-list'),
]
