from django.urls import path
from webapp.views import index_view, article_create_view, article_view

urlpatterns = [
    path('', index_view),
    path('articles/add/', article_create_view),
    path('article/', article_view)
]
