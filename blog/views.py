from django.shortcuts import render, get_object_or_404, redirect

from blog.form import CommentForm
from blog.models import Article, Category, Tag, Comment, About, Clients


# Create your views here.

def home_page(request):
    article = Article.objects.all().order_by('-id')
    context = {'articles': article}
    return render(request, 'index.html', context)


def blog_page(request):
    article = Article.objects.all().order_by('-id')
    search = request.GET.get('q')
    tags = request.GET.get('tags')
    cat = request.GET.get('cat')
    if search:
        article = article.filter(title__icontains=search)
    if tags:
        article = article.filter(tag__name=tags)
    if cat:
        article = article.filter(category__name=cat)
    context = {'articles': article}
    return render(request, 'blog.html', context)


def blog_single(request, pk):
    form = CommentForm()
    article = get_object_or_404(Article, pk=pk)
    last_2_articles = Article.objects.order_by('-id')[:2]
    categories = Category.objects.all()
    tags = Tag.objects.all()
    comments = Comment.objects.filter(article__id=pk).order_by('-id')
    recent_blogs = Article.objects.all().order_by('-id')[:3]
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            return redirect(f'/detail/{article.id}#comments')

    context = {
        'articles': article,
        'last_2_articles': last_2_articles,
        'categories': categories,
        'tags': tags,
        'comments': comments,
        'form': form,
        'recent_blogs': recent_blogs,
    }
    return render(request, 'blog-single.html', context)


def about_page(request):
    about = About.objects.all()
    team = Clients.objects.all()
    context = {'abouts': about,
               'clients': team}
    return render(request, 'about.html', context)