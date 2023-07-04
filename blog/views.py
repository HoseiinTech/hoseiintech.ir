from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, ListView

from blog.models import Portfolio, Article
from hitcount.views import HitCountDetailView


class PortfolioView(ListView):
    queryset = Portfolio.objects.filter(status=True).order_by("-created_at")
    template_name = 'blog/portfolio.html'
    context_object_name = 'portfolio_list'
    paginate_by = 6


class ProjectDetailView(DetailView):
    context_object_name = 'portfolio'
    template_name = 'blog/single-project.html'

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        project = get_object_or_404(Portfolio.objects.filter(status=True), slug=slug)
        return project


class BlogListView(ListView):
    template_name = 'blog/blog.html'
    context_object_name = 'articles'
    paginate_by = 4

    def get_queryset(self):
        articles = Article.objects.filter(status=True)
        return articles


class ArticleDetailView(HitCountDetailView):
    context_object_name = 'article'
    template_name = 'blog/single-post.html'
    count_hit = True

    def get_object(self, queryset=None):
        slug = self.kwargs.get('slug')
        article = get_object_or_404(Article.objects.filter(status=True), slug=slug)
        return article
