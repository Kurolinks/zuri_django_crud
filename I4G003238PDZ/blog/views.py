from dataclasses import fields
from djano.urls import reverse_lazy
from django.views.generic.edit import Createview, Updateview, Deleteview
from django.views.generic.list import LIstview
from django.views.generic.list import Detailview
from .models import Post

class PostCreateView(LIstView):
	model = Post
	fields = "__all__"
	success_url: reverse_lazy("blog:all")

class PostListView(LIstView):
	model = Post

class PostDetailView(DetailView):
	model = Post

class PostUpdateView(UpdateView):
	model = Post
	fields = "__all__"
	success_url: reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
	model = Post
	fields = "__all__"
	success_url: reverse_lazy("blog:all")