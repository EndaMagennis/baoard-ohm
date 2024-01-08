from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Post
from .forms import PostForm

# Create your views here.


class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "feed/index.html"
    paginate_by = 10


def post_detail(request, slug):

    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)

    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.save()

    post_form = PostForm()
    return render(
        request,
        "feed/post_detail.html",
        {
            "post": post,
        },
    )
