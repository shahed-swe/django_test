from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from .models import BlogPost
from .forms import BlogPostModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

# def blog_post_detail_page(request,post_slug):
#     obj = get_object_or_404(BlogPost, slug=post_slug)
#     # try:
#     #     obj = BlogPost.objects.get(id=post_id) #query  -> database  -> data -> django renders it
#     # except BlogPost.DoesNotExist:
#     #     raise Http404
#     # except ValueError:
#     #     raise Http404
#     template_name = 'detail.html'
#     context = {"object":obj}
#     return render(request, template_name, context)

# CRUD - Create Retrieve Update Delete

# GET - Retrieve / List
# POST - Create / Update /Delete

def blog_post_list_view(request):
    # list out objects
    #could be search
    # qs = BlogPost.objects.filter(title__icontains = "hello") #for search query
    qs = BlogPost.objects.all() #queryset -> list of python object
    template_name = 'blog/list.html'
    context = {'object_list':qs}
    return render(request, template_name, context)

# @login_required
@staff_member_required
def blog_post_create_view(request):
    #create objects
    # ? use a form
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form.save()
        form = BlogPostModelForm()
    template_name = 'form.html'
    context = {"title":"New blog",'form': form}
    return render(request, template_name, context)

def blog_post_detail_view(request,post_slug):
    #1 object -> detail view
    obj = get_object_or_404(BlogPost, slug=post_slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

def blog_post_update_view(request, post_slug):
    obj = get_object_or_404(BlogPost, slug=post_slug)
    template_name = 'blog/update.html'
    context = {"object":obj,'form': None}
    return render(request, template_name, context)

def blog_post_delete_view(request,post_slug):
    obj = get_object_or_404(BlogPost, slug=post_slug)
    template_name = 'blog/delete.html'
    context = {"object":obj}
    return render(request, template_name, context)