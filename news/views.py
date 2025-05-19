from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
import django_filters
from django_filters.views import FilterView
from django import forms
from .models import Post, News
from .forms import PostForm


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'


class NewsListView(ListView):
    model = Post
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(type='news').order_by('-created_at')


class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author__user__username = django_filters.CharFilter(lookup_expr='icontains')
    created_at = django_filters.DateFilter(lookup_expr='date',
                                           widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Post
        fields = ['title', 'author__user__username', 'created_at']


class NewsSearchView(FilterView):
    model = Post
    filterset_class = NewsFilter
    template_name = 'news/news_search.html'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(type='news').order_by('-created_at')


class NewsCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/post_form.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'news'
        post.save()
        return super().form_valid(form)


class ArticleCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'news/post_form.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type = 'article'
        post.save()
        return super().form_valid(form)


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'news/post_form.html'
    success_url = reverse_lazy('news_list')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'news/post_confirm_delete.html'
    success_url = reverse_lazy('news_list')
