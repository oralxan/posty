from django.views.generic import (
    TemplateView,
    ListView,
    DetailView
)
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy

from .models import Post

class HomePage(TemplateView):
    template_name = 'app/home.html'

class PostList(ListView):
    model = Post
    template_name = 'app/posts.html'
    context_object_name = 'postslist'

class PostDetail(DetailView):
    model = Post
    template_name = 'app/detail.html'
    context_object_name = 'post'

class PostCreate(CreateView):
    model = Post
    template_name = 'app/create.html'
    context_object_name = 'create_post'
    fields = ['title', 'description', 'image','created_date','description','price','horse_power','capacity','color','brand']
    success_url = reverse_lazy('postslist')

class PostUpdate(UpdateView):
    model = Post
    template_name = 'app/update.html'
    context_object_name = 'update_post'
    fields = ['title', 'description', 'image','created_date','description','price','horse_power','capacity','color','brand']
    success_url = reverse_lazy('postslist')

class PostDelete(DeleteView):
    model = Post
    template_name = 'app/delete.html'
    context_object_name = 'delete_posts'
    success_url = reverse_lazy('postslist')