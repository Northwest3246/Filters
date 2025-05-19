import django_filters
from django import forms
from .models import Post

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    author_name = django_filters.CharFilter(field_name='author__username', lookup_expr='icontains')
    date = django_filters.DateFilter(
        field_name='published_date',
        lookup_expr='date',
        widget=forms.DateInput(attrs={'type':'date'}))

    class Meta:
        model = Post
        fields = ['title', 'author_name', 'date']