from django.urls import path
from webapp.views import index_view, article_create_view, article_view

urlpatterns = [
    path('', index_view, name='index'),
    path('articles/add/', article_create_view, name='article_create'),
    path('article/<int:pk>/details/', article_view, name='article_view')
]
