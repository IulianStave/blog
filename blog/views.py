from django.shortcuts import render
#from django.http import HttpResponse


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
#   return HttpResponse('<h1> Blog home</h1')
    context = {
        'posts':posts
    }
    return render(request, 'blog/home.html', context)
def about(request):
#   return HttpResponse('<h1> Blog about</h1>')
    return render(request, 'blog/about.html')
