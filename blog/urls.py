from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView

urlpatterns = [
    path("post/<int:pk>/edit", BlogUpdateView.as_view(), name="post_edit"),
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    # All blog posts entries will start with post/. int:pk, the primary key, is an id that django automatically adds to our db models which numbers our, in this case, post. We can access it either as id, or pk
    # pk for our first post "Hello, World!" is 1, the second is 2 and so on. It'll look like post/1/
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
    # The empty string tells python to match all values
    path("", BlogListView.as_view(), name="home"),
    
]