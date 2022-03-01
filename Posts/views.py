from django.shortcuts import render
from django.views.generic import DetailView, TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from .forms import PostCreateForm


def post_list_view(request):
    """Published posts list view"""
    post_list = Post.objects.filter(publish_date__isnull=False).order_by('-publish_date')

    paginator = Paginator(post_list, 1)
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)

    return render(request, 'posts/posts.html', {'page_obj': post})


def post_draft_list_view(request):
    """Unpublished posts list view"""
    post_draft_list = Post.objects.filter(publish_date__isnull=True).order_by('-create_date')

    paginator = Paginator(post_draft_list, 1)
    page_number = request.GET.get('page')
    post_draft = paginator.get_page(page_number)

    return render(request, 'posts/posts_draft.html', {'page_obj': post_draft})


class PostDetailView(DetailView):
    """Published post DetailView"""
    model = Post
    template_name = 'posts/post_detail.html'

    def get_queryset(self):
        queryset = super(PostDetailView, self).get_queryset()
        return queryset.filter(publish_date__isnull=False)


class PostDraftDetailView(DetailView):
    """Unpublished post DetailView"""
    model = Post
    template_name = 'posts/post_draft_detail.html'

    def get_queryset(self):
        queryset = super(PostDraftDetailView, self).get_queryset()
        return queryset.filter(publish_date__isnull=True)


@login_required
def publish_post(request, slug):
    """Publishing post"""
    post = Post.objects.get(slug=slug)

    post.publish_date = datetime.datetime.now()
    return HttpResponseRedirect(reverse('posts:post_detail', kwargs={'slug': slug}))


class TestView(TemplateView):
    template_name = 'posts/post_add.html'
    form_class = PostCreateForm


@login_required()
def post_create_view(request):
    """Post creation view"""
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST)

    else:
        return render(request, 'posts/post_add.html', {'form': form})
