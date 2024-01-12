from typing import Any
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Post
from .forms import PostForm

# Create your views here.


class PostList(generic.ListView):
    ''' List all posts '''

    queryset = Post.objects.all()
    template_name = "feed/index.html"
    paginate_by = 8


class AddPost(View):
    '''Add a new post'''

    def get(self, request: Any) -> Any:
        '''Render the form'''
        form = PostForm()
        return render(request, "feed/post_create.html", {"form": form})
    
    def post(self, request: Any) -> Any:
        '''Create a new post'''
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(post.title)
            post.image = request.FILES.get("image")
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

    def check_user(self, request):
        '''Check if user is the author of the post'''
        post = get_object_or_404(Post, slug=self.kwargs.get("slug"))
        if request.user == post.author:
            return True
        else:
            return False
    
    def update_post(self, request):
        '''Update the post'''
        form = self.form_class(request.POST, request.FILES, instance=self.get_object())
        if form.is_valid():
            form.save()
            return True
        else:
            return False
    

    
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
    


@login_required
def like(request):
    '''Like a post'''
    if request.method == "POST":
        result = ''
        id = int(request.POST.get("post_id"))
        post = get_object_or_404(Post, id=id)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            post.number_of_likes -= 1
            result = post.number_of_likes
            post.save()
        else:
            post.likes.add(request.user)
            post.number_of_likes += 1
            result =  post.number_of_likes
            post.save()

        return JsonResponse({"result": result})
