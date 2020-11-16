from django.urls import path,include
from .views import IndexView,PostDetailView,CategoryListView,TagListView,CategoryPostView,TagPostView,SearchPostView,CommentFormView,ReplayFormView,comment_approve,comment_remove,reply_approve,reply_remove
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
    path('',IndexView.as_view(),name="index"),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post_detail'),
    path('categories/',CategoryListView.as_view(),name='category_list'),
    path('tag/',TagListView.as_view(),name='tag_list'),
    path('category/<str:category_slug>',CategoryPostView.as_view(),name='category_post'),
    path('tag/<str:tag_slug>/',TagPostView.as_view(),name='tag_post'),
    path('search/',SearchPostView.as_view(),name='search_post'),
    path('comment/<int:pk>/', CommentFormView.as_view(), name='comment_form'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
    path('reply/<int:pk>/', ReplayFormView.as_view(), name='reply_form'),
    path('reply/<int:pk>/approve/', reply_approve, name='reply_approve'),
    path('reply/<int:pk>/remove/', reply_remove, name='reply_remove'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)