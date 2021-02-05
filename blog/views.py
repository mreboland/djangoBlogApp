# Importing ListView and our db model Post
from django.views.generic import ListView, DetailView
from .models import Post

# Subclassing ListView and adding links to our model and template
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"