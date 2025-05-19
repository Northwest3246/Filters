from django.urls import path
from . import views

urlpatterns = [
    path('', views.NewsListView.as_view(), name='news_list'),
    path('<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('search/', views.NewsSearchView.as_view(), name='news_search'),
    path('create/', views.NewsCreateView.as_view(), name='news_create'),
    path('article/create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),
]