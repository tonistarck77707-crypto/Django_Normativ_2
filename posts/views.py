from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm

def test_post_create(request):
    post = Post.objects.create(title="Test Post", content="Soft delete test")
    return render(request, 'store/test_post.html', {'post': post})