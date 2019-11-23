from django.shortcuts import render

posts = [
    {
        'author':'CoreyMS',
        'title':'Blog Post one',
        'content':'First post content',
        'date_posted':'August 27,2018'
    },
    {
        'author':'Stave Iulian',
        'title':'Blog Stave Post',
        'content':'Second post content',
        'date_posted':'August 7,2018'
    }
]
def home(request):
    context = {
        'posts': posts,
        'title' : 'Blog Home',
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title': 'About blog'})
