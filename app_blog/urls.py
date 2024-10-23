# app_blog/urls.py

from django.urls import path
from .views import (HomePageView, ArticleDetail, ArticleList, ArticleCategoryList)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('articles', ArticleList.as_view(), name='articles-list'),
    path('articles/category/<slug>/', ArticleCategoryList.as_view(), name='articles-category-list'),
    path('articles/<int:year>/<int:month>/<int:day>/<slug>/', ArticleDetail.as_view(), name='news-detail'),
]
