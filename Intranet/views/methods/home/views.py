from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect

import random

from News.models.post.models import PostModel


def get_random_post(length):
    return random.randint(0, length-1)


def get_length(queryset):
    return len(queryset)


#                                                                                                            RENDER HOME
def render_home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('welcome'))

    posts = PostModel.objects.all()
    posts_length = get_length(posts)

    if posts_length < 8:
        context = {
            'HOME': True,
            'have_posts': False
        }
    else:
        number = get_random_post(posts_length)

        while abs(number - posts_length) < 8:
            number = get_random_post(posts_length)

        context = {
            'HOME': True,

            'have_posts': True,

            'left_featured_post': posts[number:number+1],
            'left_small_posts': posts[number+1:number+4],

            'right_featured_post': posts[number+4:number+5],
            'right_small_posts': posts[number+5:number+8]
        }

    return render(
        request,
        'singles/home/template/template_home.html',
        context=context
    )
