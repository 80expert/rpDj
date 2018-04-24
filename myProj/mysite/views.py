from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def homepage(request):
    template = get_template("homepage.html")
    posts = Post.objects.all()
    post_lists = []
    for count, post in enumerate(posts):
        post_lists.append(str(post.title) +": "+ str(post.slug) + '<br>')
    return HttpResponse(post_lists)

def do_insert(request):
    title=request.GET('title')
    post = models.Post.objects.create(title='title')
    post.save()
    return render(request,'/')
