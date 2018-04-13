from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Blog
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
	# return render(request, template_name)