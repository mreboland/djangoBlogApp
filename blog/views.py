# Importing ListView and our db model Post
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import Post

# Subclassing ListView and adding links to our model and template
class BlogListView(ListView):
    model = Post
    template_name = "home.html"

# We define the model we're using, Post, and the template we want it associated with, post_detail. DetailView will provide a context object we can use in our template called either 'object' or the lowercased name of our model, 'post'. DetailView also expects either a primary key or a slug passed to it as the identifier.
class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    
# We specify our db model Post, the name of our template post_new.html. For fields we explicitly set the db fields we want to expose which are title, author, and body.
class BlogCreateView(CreateView):
    model = Post
    template_name = "post_new.html"
    fields = [
        "title",
        "author",
        "body"
        ]