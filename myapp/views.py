from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

from .forms import BlogForm
from .models import Blog


def home(request):

    if request.method == "POST":

        form = BlogForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect("home")

    else:

        form = BlogForm()

    blogs = Blog.objects.all().order_by("-created_at")

    context = {
        "form": form,
        "blogs": blogs,
    }

    return render(request, "home.html", context)


def edit_blog(request, id):

    blog = get_object_or_404(Blog, id=id)

    if request.method == "POST":

        form = BlogForm(request.POST, request.FILES, instance=blog)

        if form.is_valid():

            form.save()

            return redirect("home")

    else:

        form = BlogForm(instance=blog)

    context = {
        "form": form,
        "blog": blog,
    }

    return render(request, "edit_blog.html", context)
