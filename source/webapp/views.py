from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from webapp.models import Article


def index_view(request):
    articles = Article.objects.all()
    return render(request, 'index.html', {'articles': articles})


def article_view(request, *args, pk, **kwargs):
    # article = Article.objects.get(id=pk)
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'article_view.html', {'article': article})


def article_create_view(request):
    if request.method == "GET":
        return render(request, 'article_create.html')
    elif request.method == "POST":
        article = Article.objects.create(
            title=request.POST.get('title'),
            content=request.POST.get('content'),
            author=request.POST.get('author')
        )
        # url = reverse('article_view', kwargs={'pk': article.pk})
        # return HttpResponseRedirect(url)
        return redirect('article_view', pk=article.pk)
        # return HttpResponseRedirect(f'/article/{article.pk}/')

    # return HttpResponseRedirect('/')
