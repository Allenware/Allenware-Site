
from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def post_index(request):
    """
        An index view show a snippet of information about each post
    :param request:
    :return:
    """

    posts = Post.objects.all()
    context = {'posts': posts}

    return render(request, 'post/index.html', context)


def post_detail(request, post_id):
    """
        A detail view that shows more information on a particular post
    :param request:
    :param post_id
    :return:
    """

    post = Post.objects.get(pk=post_id)
    context = {
        'post': post
    }
    return render(request, 'post/detail.html', context)
