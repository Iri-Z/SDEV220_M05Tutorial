from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

#Sort the posts by published date and return to the posts page for display
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

#Display only the selected post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

#Render the file with form for creating a new post or send new post details
def post_new(request):
    #Check if we are opening the page or sending a new post
    if request.method == "POST":
        #Check everything is okay
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            #Send to the newly created post's page
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    #Load the form page
    return render(request, 'blog/post_edit.html', {'form': form})

#Editing post page
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    #Check if we are getting the edit page or sending updated post details
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})