from django.urls import path
from .views import BlogListView


urlpattterns = [
    path('', BlogListView.as_view(), name='name')
,]