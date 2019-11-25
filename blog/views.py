from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
                                    ListView,
                                    DetailView,
                                    CreateView,
                                    DeleteView,
                                    UpdateView
)

# function based views
def home(request):
    context = {
        'posts': Post.objects.all(),
        'title' : 'Blog Home',
    }
    return render(request, 'blog/home.html', context)



# class based views - built-in functionalities - ListView

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html' #<app>/<model>_<list>.html => blog/post_list.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']

    #override the form valid method form_valid()
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
 

class PostDeleteView(DeleteView):
    model = Post


def about(request):
    return render(request, 'blog/about.html',{'title': 'About blog'})
    