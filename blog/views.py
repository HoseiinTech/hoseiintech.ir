from django.shortcuts import render


def portfolio(request):
    return render(request, 'blog/portfolio.html')


def blog(request):
    return render(request, 'blog/blog.html')
