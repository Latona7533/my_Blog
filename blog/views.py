from django.core.paginator import Paginator, PageNotAnInteger
from .models import Post
from django.shortcuts import render,get_object_or_404
from .forms import CommentForm

def posts_view(request):
    posts =Post.objects.all()
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    return render(request, 'posts.html', {'posts': posts, 'page': page,})

def post_view(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comment.filter(active=True)
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post =post
            form.save()
    return render(request, 'post.html', {'post': post, 'comments' : comments, 'form': form})
