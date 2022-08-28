from django.shortcuts import render
from .models import Post
 
posts =[
        {
                'author': 'corey',
                'title' : 'Blog Post 1',
                'content': 'first post content',
                'date_posted': 'Augest 23 2022',
        },
         {
                'author': 'John doe',
                'title' : 'Blog Post 2',
                'content': 'secpnd post content',
                'date_posted': 'Augest 25 2022',
        },
        
]

def home(request):
        context = {
                'posts': Post.objects.all()
        }
        return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')