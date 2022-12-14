from django.urls import path, include
from main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authors', views.authors, name='authors'),
    
    path('article/<int:pk>', views.article, name='get_article'),
    path('author/<int:pk>', views.author, name='get_author'),

    path('article', views.create_article, name='create_article'),
    path('author', views.create_author, name='create_author'),

]
