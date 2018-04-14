from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseForbidden, HttpResponseRedirect
from .models import Blog, Comment
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
	blog_list = Blog.objects.order_by('-pub_date')
	context = {"blog_list":blog_list}

	if request.user.is_authenticated:
		context["user"] = request.user

	return render(request, 'blogger/index.html', context)

def detail(request, blog_id):
	try:
		blog = Blog.objects.get(pk=blog_id)
		context = {"blog":blog}
	except:
		raise Http404("Blog does not exist")

	return render(request, "blogger/detail.html", context)

@login_required()
def new_blog_page(request):
	return render(request, 'blogger/new_blog.html')

@login_required()
def create_new_blog(request):
	b = Blog.objects.create(title=request.POST['title'], 
		content=request.POST['content'], 
		author = request.user,
		pub_date=timezone.now())
	return HttpResponseRedirect(reverse('index'))

@login_required()
def delete_blog(request, blog_id):
	try:
		b = Blog.objects.get(id=blog_id)
		if request.user.username==b.author.username:
			b.delete()
		else:
			return HttpResponseForbidden("You do not have permission to do this")
	except:
		raise Http404("Blog does not exist")

	return HttpResponseRedirect(reverse('index'))

@login_required()
def create_comment(request, blog_id):
	Comment.objects.create(text=request.POST['comment_text'], 
		blog_id=blog_id, 
		commenter=request.user,
		pub_date=timezone.now())
	return HttpResponse("Done")

@login_required()
def delete_comment(request, comment_id):
	try:
		c = Comment.objects.get(id=comment_id)
		if request.user.username==c.commenter.username:
			c.delete()
		else:
			return HttpResponseForbidden("You do not have permission to do this")
	except:
		raise Http404("Comment does not exist")

	return HttpResponse("Done")	
