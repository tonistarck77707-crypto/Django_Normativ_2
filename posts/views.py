#from django.shortcuts import render, redirect
#from .models import Post
#from .forms import PostForm

#def test_post_create(request):
 #   post = Post.objects.create(title="Test Post", content="Soft delete test")
  #  return render(request, 'store/test_post.html', {'post': post})

from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Post


def post_list(request):
    q = request.GET.get("q")

    posts = Post.objects.all()

    if q:
        posts = posts.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q)
        )


    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "q": q,
    }
    return render(request, "posts/post_list.html", context)