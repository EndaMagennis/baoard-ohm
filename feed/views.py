from typing import Any
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib import messages
from .models import Post
from .forms import PostForm

# Create your views here.


class PostList(generic.ListView):
    ''' List all posts '''

    queryset = Post.objects.all()
    template_name = "feed/index.html"
    paginate_by = 10


class AddPost(View):
    '''Add a new post'''

    def get(self, request: Any) -> Any:
        form = PostForm()
        return render(request, "feed/post_create.html", {"form": form})

    def post(self, request: Any) -> Any:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = post.title.replace(" ", "-")
            post.save()
            messages.add_message(request, messages.SUCCESS, "Post created successfully")
            return redirect("home")
        else:
            messages.add_message(request, messages.ERROR, "Post creation failed")
            return render(request, "feed/post_create.html", {"form": form})

class PostRead(generic.DetailView):
    '''Read a post'''

    model = Post
    template_name = "feed/post_read.html"
    
class PostUpdate(generic.UpdateView):
    '''Update a post'''

    model = Post
    template_name = "feed/post_update.html"
    form_class = PostForm
    success_url = "/"

    def form_valid(self, form):
        messages.success(self.request, "Post updated successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "Post update failed")
        return super().form_invalid(form)
    
class PostDelete(generic.DeleteView):
    '''Delete a post'''
    
    model = Post
    template_name = "feed/post_delete.html"
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Post deleted successfully")
        return super().delete(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        messages.error(self.request, "Post deletion failed")
        return super().post(request, *args, **kwargs)
    

