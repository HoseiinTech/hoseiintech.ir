from django.urls import path, re_path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
    re_path('portfolio/detail/(?P<slug>[-\w]+)/$', views.ProjectDetailView.as_view(), name='project-detail'),
    path('blog/', views.BlogListView.as_view(), name='blog'),
    re_path('blog/detail/(?P<slug>[-\w]+)/$', views.ArticleDetailView.as_view(), name='blog-detail')
]
