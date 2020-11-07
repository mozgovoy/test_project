from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Post


class MainPageView(ListView):
    template_name="pages/main.html"
    model=Post
    context_object_name='all_posts_list'