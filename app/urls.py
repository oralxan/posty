from django.urls import path

from .views import (
    HomePage,
    PostList,
    PostDetail,
    PostCreate,
    PostUpdate,
    PostDelete
)

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('posts/', PostList.as_view(), name='postslist'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post'),
    path('posts/create/', PostCreate.as_view(), name='post_create'),
    path('posts/update/<int:pk>/', PostUpdate.as_view(), name='post_update'),
    path('posts/delete/<int:pk>/', PostDelete.as_view(), name='posts')
]