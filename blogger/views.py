from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Blog
from django.utils import timezone
from django.urls import reverse
# Create your views here.

def index(request):
	blog_list = Blog.objects.order_by('-pub_date')
	context = {"blog_list":blog_list}
	return render(request, 'blogger/index.html', context)

def detail(request, blog_id):
	try:
		blog = Blog.objects.get(pk=blog_id)
		context = {"blog":blog}
	except:
		raise Http404("Blog does not exist")

	return render(request, "blogger/detail.html", context)

def new_blog_page(request):
	return render(request, 'blogger/new_blog.html')

def create_new_blog(request):
	b = Blog.objects.create(title=request.POST['title'], content=request.POST['content'], pub_date=timezone.now())
	return HttpResponseRedirect(reverse('index'))

def delete_blog(request, blog_id):
	try:
		Blog.objects.get(id=blog_id).delete()
	except:
		raise Http404("Blog does not exist")

	return HttpResponseRedirect(reverse('index'))