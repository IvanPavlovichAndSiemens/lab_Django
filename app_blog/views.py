from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Article, Category


class HomePageView(ListView):
    model = Article
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(main_page=True)[:5]
        return context

    def get_queryset(self, *args, **kwargs):
        categories = Category.objects.all()
        return categories


class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'item'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetail, self).get_context_data(*args, **kwargs)
        try:
            context['images'] = context['item'].images.all()
        except:
            pass
        return context


class ArticleList(ListView):
    model = Article
    template_name = 'articles_list.html'
    context_object_name = 'items'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleList, self).get_context_data(*args, **kwargs)
        try:
            context['category'] = Category.objects.get(slug=self.kwargs.get('slug'))
        except Exception:
            context['category'] = None
        return context

    def get_queryset(self, *args, **kwargs):
        articles = Article.objects.all()
        return articles


class ArticleCategoryList(ArticleList):
    def get_queryset(self, *args, **kwargs):
<<<<<<< HEAD
        articles = Article.objects.filter(
            category__slug=self.kwargs['slug']
        ).distinct()
        return articles


class CategoryMainArticleView(DetailView):
    model = Category
    template_name = 'category_main.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        # Знайти головну публікацію категорії
        context['main_article'] = Article.objects.filter(
            category=category,
            main_page=True
        ).first()
        return context
=======
        articles = Article.objects.filter(category__slug__in=[self.kwargs['slug']]).distinct()
        return articles
>>>>>>> f313550be5bd4149964152af4e173e8586d50ae5
