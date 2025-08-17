from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="blog/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="blog/logout.html"),
        name="logout",
    ),
]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls")),
]


# blog/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    # Post CRUD URLs
    path("", PostListView.as_view(), name="post-list"),
    path("posts/new/", PostCreateView.as_view(), name="post-create"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    # Auth URLs
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="blog/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="blog/logout.html"),
        name="logout",
    ),
]


from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register,
    profile,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Blog post CRUD views
    path("", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    # Authentication views
    path("register/", register, name="register"),
    path("profile/", profile, name="profile"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="blog/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="blog/logout.html"),
        name="logout",
    ),
]

# Comment URLs
path("post/<int:post_id>/comments/new/", views.add_comment, name="add-comment"),
path("comments/<int:pk>/edit/", views.edit_comment, name="edit-comment"),
path("comments/<int:pk>/delete/", views.delete_comment, name="delete-comment"),


from .views import (
    # other views...
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns += [
    path(
        "post/<int:post_id>/comments/new/",
        CommentCreateView.as_view(),
        name="add-comment",
    ),
    path("comments/<int:pk>/edit/", CommentUpdateView.as_view(), name="edit-comment"),
    path(
        "comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="delete-comment"
    ),
]

from django.urls import path
from .views import (
    # other views...
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns += [
    path(
        "post/<int:pk>/comments/new/",
        CommentCreateView.as_view(),
        name="comment-create",
    ),
    path(
        "comment/<int:pk>/update/", CommentUpdateView.as_view(), name="comment-update"
    ),
    path(
        "comment/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment-delete"
    ),
]


from django.urls import path
from .views import SearchResultsView, TaggedPostListView

urlpatterns += [
    path("search/", SearchResultsView.as_view(), name="search-results"),
    path("tags/<str:tag>/", TaggedPostListView.as_view(), name="posts-by-tag"),
]


from .views import PostByTagListView

path("tags/<slug:tag_slug>/", PostByTagListView.as_view(), name="posts-by-tag"),
