from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,JsonResponse,FileResponse
from django.template import loader
from .models import Blog

def showBlog(request,blogId):
    template = loader.get_template('blog.html')
    blog = Blog.objects.get(id=blogId)
    context = {'blog':blog}
    html = template.render(context)
    return HttpResponse(html)

def showBlogList(request):
    template = loader.get_template('blog_list.html')
    blogs = Blog.objects.all()
    context = {'blogs':blogs}
    html = template.render(context)
    return HttpResponse(html)
