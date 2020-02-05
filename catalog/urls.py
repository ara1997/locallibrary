from django.conf.urls import url, re_path
from django.urls import path, re_path
from . import views



app_name='catalog'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    # path('', views.index, name='index'),
    path('books/', views.BooKListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    re_path('^book/(?P<pk>\d+)', views.BookDetailView.as_view(), name='book-detail'),
    #url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]
