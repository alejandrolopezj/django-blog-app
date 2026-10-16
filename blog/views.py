from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic.list import ListView

from blog.forms import CommentForm
from blog.models import Post


class StartingPageView(ListView):
    template_name = "blog/starting_page.html"
    model = Post
    ordering = "-date"
    context_object_name = "latest_posts"
    paginate_by = 3


class PostView(ListView):
    template_name = "blog/posts.html"
    model = Post
    ordering = "-date"
    context_object_name = "post_list"


class PostDetailView(View):
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        context = {
            "post": post,
            "form": CommentForm(),
        }
        return render(request, "blog/post_detail.html", context)

    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse("blog:post-detail-page", args=[slug]))

        context = {
            "post": post,
            "form": form,
        }
        return render(request, "blog/post_detail.html", context)
