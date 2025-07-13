from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('send/', views.write, name='send'),
    path('sub/', views.subscribe, name='sub'),
    path('view/', views.show_topics, name='view'),
    path('spam/', views.start_spam, name='spam')
]
