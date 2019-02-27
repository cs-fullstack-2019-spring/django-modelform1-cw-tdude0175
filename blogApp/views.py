from django.shortcuts import render
from django.http import HttpResponse
from .forms import BlogPostForm
# Create your views here.

def index(request):
    blogPost = BlogPostForm()

    if(request.method == "POST"):
        print(request.POST)
        blogPost = BlogPostForm(request.POST)
        if(blogPost.is_valid()):  #makes sure the feilds are valid
            blogPost.save(commit=True)
            return render(request, 'blogApp/completePost.html')
    # will return form if form is newly rendered
    content =\
        {
            'BlogForm':blogPost
        }
    return render(request,'blogApp/index.html',content)