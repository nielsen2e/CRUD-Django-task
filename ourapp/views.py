from django.shortcuts import render
from django.views.generic import Listview
from .models import Post,comment
from .forms import CommentForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms import ModelForm, widgets


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
 
  = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment_new.html'
    widgets = {
            'post': widgets.HiddenInput
        }

    def form_valid(self, form ):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')

class CommentCreateView():
    m

def Dashboard(request):
    return render(request, "dashboard.html")