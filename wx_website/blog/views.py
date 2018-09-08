from django.shortcuts import render

# Create your views here.
from blog.models import Article


# Create your views here.
def blog_index(request):
    blog_list = Article.objects.all()  # get all data
    return render(request,'index.html', {'blog_list':blog_list})   #return index.html page
