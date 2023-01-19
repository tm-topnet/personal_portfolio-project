from django.shortcuts import render, get_object_or_404
from .models import Bloggo

# Create your views here.
def all_blogs(request):

    blogs = Bloggo.objects.all() # order_by('-date')[:5]

    return render(request, 'blog/all_blogs.html',{'blogs':blogs})

def detail(request, blog_id):

    blog = get_object_or_404(Bloggo, pk=blog_id) #pk = primarykey
    
    return render(request, 'blog/detail.html',{'blog':blog})