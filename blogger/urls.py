from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('<int:blog_id>/', views.detail, name="detail"),
	path('new_blog_page/', views.new_blog_page, name="new_blog_page"),
	path('new_blog_submit/', views.create_new_blog, name="create_new_blog"),
	path('<int:blog_id>/delete/', views.delete_blog, name="delete_blog"),
]