from django.db import models
# Reverse is a utility function django provides us to reference and object by its URL template name. In our case, post_detail.
from django.urls import reverse

# Characteristics of a typical blog will have a title, author, and body. We will need to model this behaviour.


class Post(models.Model):
    # We are limiting the title of the post fo 200 characters
    title = models.CharField(max_length=200)
    # ForeignKey allows for a many-to-one relationship. This means that a given user can be the author of many different blog posts but not the other way around. This is built into django and we also must specify an on_delete option.
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE
    )
    # Using TextField automatically expands as needed to fit user's text
    body = models.TextField()
    
    def __str__(self):
        return self.title

    # When we submit a form we get a 'no URL to redirect to' error. It results because we did not specify where to send the user after successfully submitting the form.
    # get_absolute_url is a best practicethat we should always do. It sets a canonical URL for an object so even if the structure of our URLs change, the reference to the specific object is the same.
    # Because our post_detail uses a primary key (pk), we need to reference that id when we use 'reverse'. pk and id are interchangeable, the reason we use id here is django docs recommend using self.id with get_absolute_url.
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
