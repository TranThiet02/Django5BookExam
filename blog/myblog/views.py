from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404 

def post_list(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'blog/post/list.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id=id,
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )