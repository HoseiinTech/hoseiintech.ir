from django.urls import path
from home import views

app_name = 'home'
urlpatterns = [
    path('', views.AboutMeView.as_view(), name='about'),
    path('resume/', views.MyResumeView.as_view(), name='resume'),
    path('contact/', views.contact, name='contact')
]
