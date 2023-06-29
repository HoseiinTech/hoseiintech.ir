from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog')
]
