from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Post_Form
from .models import Post

# Create Post 
def vw_CreatePost(request):
    if request.method == 'POST':
        formPost = Post_Form(request.POST)
        if formPost.is_valid():
            # Below Code Also work
            #formPost.save()

            # Can Save Individual Field as Below
            post_title = formPost.cleaned_data['post_title']
            post_content = formPost.cleaned_data['post_content']
            post_type = formPost.cleaned_data['post_type']
            post_status = formPost.cleaned_data['post_status']
            post_additionalContext = formPost.cleaned_data['post_additionalContext']
            objPost = Post(
                post_title=post_title, 
                post_content=post_content, 
                post_type=post_type, 
                post_status=post_status,
                post_additionalContext=post_additionalContext
                )
            objPost.save()
            return redirect('/post/')
    else:
        formPost = Post_Form()
    return render(request, 'Post/create_post.html', {'form': formPost})
    #return HttpResponse("Hello Creating Post")

#   Get Post List
def vw_ViewPost(request):
        allPost = Post.objects.all()
        return render(request, 'Post/view_post.html', {'Posts': allPost})
        #return HttpResponse("View Post")

def vw_DeletePost(request, id):
    if request.method == 'POST':
        pi = Post.objects.get(pk=id)
        pi.delete()
        return redirect('/post/')

