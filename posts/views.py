from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post

@login_required
def create_post(request):

    if request.user.role != "SENIOR":
        return redirect('dashboard')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()

            return redirect('post_list')

    else:
        form = PostForm()

    return render(request, 'create_post.html', {'form': form})


@login_required
def post_list(request):

    posts = Post.objects.all().order_by('-created_at')

    return render(request, 'post_list.html', {'posts': posts})
