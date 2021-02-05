from django.db import models

# Characteristics of a typical blog will have a title, author, and body. We will need to model this behaviour.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        "auth.User",
        on_delete=models.CASCADE
    )
    body = models.TextField()
    
    def __str__(self):
        return self.title
