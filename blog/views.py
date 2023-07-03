from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from blog.models import Portfolio, Category


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


def blog(request):
    return render(request, 'blog/blog.html')
