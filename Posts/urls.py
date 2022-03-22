from django.urls import path
from .views import (post_list_view, PostDetailView, post_create_view, post_draft_list_view, PostDraftDetailView,
                    publish_post, PostDeleteView, PostEditView)

app_name = 'Posts'

urlpatterns = [
    path('list/', post_list_view, name='post_list'),
    path('draft_list/', post_draft_list_view, name='post_draft_list'),
    path('create/', post_create_view, name='post_create'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('draft/<slug:slug>/', PostDraftDetailView.as_view(), name='post_draft_detail'),
    path('publish/<slug:slug>', publish_post, name='post_publish'),
    path('delete/<slug:slug>', PostDeleteView.as_view(), name='post_delete'),
    path('edit/<slug:slug>', PostEditView.as_view(), name='post_edit')
]
