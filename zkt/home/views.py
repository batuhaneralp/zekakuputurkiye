from posts.models import Post
from django.shortcuts import render

def index(request):
    posts_data = Post.objects.all()

    context = {
        "posts":posts_data
    }

    return render(request,"index.html",context = context)
