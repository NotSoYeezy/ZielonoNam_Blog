from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, DeleteView, UpdateView
from django.core.paginator import Paginator
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from .forms import PostCreateForm
from django.urls import reverse_lazy
from django.contrib import messages
import random

# Importing config variables for FireBase
from ZielonoNam.settings import THUMBNAILS_DIR, storage


def post_list_view(request):
    """Published posts list view"""
    post_list = Post.objects.filter(publish_date__isnull=False).order_by('-publish_date')

    paginator = Paginator(post_list, 1)
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)

    return render(request, 'posts/posts.html', {'page_obj': post})


@user_passes_test(lambda u: u.is_superuser)
@login_required()
def post_draft_list_view(request):
    """Unpublished posts list view"""
    post_draft_list = Post.objects.filter(publish_date__isnull=True).order_by('-create_date')

    paginator = Paginator(post_draft_list, 1)
    page_number = request.GET.get('page')
    post_draft = paginator.get_page(page_number)

    return render(request, 'posts/posts.html', {'page_obj': post_draft})


class PostDetailView(DetailView):
    """Published post DetailView"""
    model = Post
    template_name = 'posts/post_detail.html'

    def get_queryset(self):
        queryset = super(PostDetailView, self).get_queryset()
        return queryset.filter(publish_date__isnull=False)


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class PostDraftDetailView(DetailView, LoginRequiredMixin):
    """Unpublished post DetailView"""
    login_url = '/user/login/'
    model = Post
    template_name = 'posts/post_detail.html'

    def get_queryset(self):
        queryset = super(PostDraftDetailView, self).get_queryset()
        return queryset.filter(publish_date__isnull=True)


@user_passes_test(lambda u: u.is_superuser)
@login_required
def publish_post(request, slug):
    """Publishing post"""
    post = Post.objects.get(slug=slug)

    post.publish()
    return HttpResponseRedirect(reverse('Posts:post_list'))


@user_passes_test(lambda u: u.is_superuser)
@login_required()
def post_create_view(request):
    """Post creation view"""
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.author = request.user
            file = form.cleaned_data['thumbnail']
            form.save()
            post = Post.objects.get(title=form.instance.title)
            n = random.randint(2150, 195213)
            storage.child(THUMBNAILS_DIR + f'{n}_{file.name}').put(file)
            post.cdn_url = storage.child(THUMBNAILS_DIR + f'{n}_{file.name}').get_url(None)
            print(post.cdn_url)
            post.save()
            return HttpResponseRedirect(reverse('Posts:post_draft_list'))
        else:
            messages.info(request, form.errors)
            return render(request, 'posts/post_add.html', {'form': form})
    else:
        return render(request, 'posts/post_add.html', {'form': form})


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class PostDeleteView(DeleteView, LoginRequiredMixin):
    login_url = '/user/login/'
    model = Post
    success_url = reverse_lazy('Posts:post_list')


@method_decorator(user_passes_test(lambda u: u.is_superuser), name='dispatch')
class PostEditView(UpdateView, LoginRequiredMixin):
    login_url = '/user/login/'
    model = Post
    fields = ['title', 'content', 'thumbnail']
    template_name = 'posts/post_add.html'
    success_url = reverse_lazy('Posts:post_list')
