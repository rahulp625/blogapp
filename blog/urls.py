from django.urls import path
from . import views
from .views import *
urlpatterns = [
#     blogs
    path("", PostList.as_view(), name="blogs"),
    path('posts/', PostList.as_view(), name="blogs"),
    path('post/add', PostCreateView.as_view(), name='post-add'),
    path('post/<slug:slug>', views.PostDetail.as_view(), name='post_detail'),

    # path('<int:id>/', views.PostDetail.as_view(), name='post_detail'),
    # path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("post/<str:slug>/edit", UpdatePostView.as_view(), name="edit_blog_post"),
    
    path("post/<str:slug>/confirm-delete", confirm_post_delete, name="confirm_delete_blog_post"),
    path("post/<int:pk>/delete", DeletePostView.as_view(), name="delete_blog_post"),
    # path("delete_blog_post/<str:slug>/", views.Delete_Blog_Post, name="delete_blog_post"),

#    user authentication
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]
                                                                                                                                                          