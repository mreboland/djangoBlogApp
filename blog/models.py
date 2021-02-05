from django.db import models

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
