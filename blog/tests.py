# We import get_user_model to reference our active User and TestCase
from django.contrib.auth import get_user_model
from django.http import response
from django.test import TestCase
from django.urls import reverse

from .models import Post

# We want to ensure that the Post model works as well as its str representation. We also want to test ListView and DetailView.

class BlogTests(TestCase):
    
    def setUp(self):
        # We create a test user
        self.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret"
        )
        # We create a sample blog post to test 
        self.post = Post.objects.create(
            title="A good title",
            body="Nice body content",
            author=self.user,
        )

    # The next two tests then confirm that both it's string representation and content are correct.
    def test_string_representation(self):
        post = Post(title="A simple title")
        self.assertEqual(str(post), post.title)
        
    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "A good title")
        self.assertEqual(f"{self.post.author}", "testuser")
        self.assertEqual(f"{self.post.body}", "Nice body content")
    
    # We confirm that our homepage return a 200 http status code, contains our body text, and uses the correct home.html template.
    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Nice body content")
        self.assertTemplateUsed(response, "home.html")
    
    # We test that our detail page works as expected and that an incorrect page returns a 404.
    def test_post_detail_view(self):
        response = self.client.get("/post/1/")
        no_response = self.client.get("/post/100000")
        self.assertEqual(response.status_code, 200)
        # The below generates a 301 and not a 404, generating a failure. This contradicts the lesson which says it should be a 404.
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "A good title")
        self.assertTemplateUsed(response, "post_detail.html")
    

    # To test create view we make a new response and then ensure that the response goes through(status code 200) and contains our new title and body text
    def test_post_create_view(self):
        response = self.client.post(reverse("post_new"), {
            "title": "New title",
            "body": "New text",
            "author": self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertContains(Post.objects.last().title, "New title")
        self.assertEqual(Post.objects.last().body, "New text")
        
    # For update view we access the first post–which has a pk of 1 which is passed in as the only argument–and we confirm that it results in a 302 redirect
    def test_post_update_view(self):
        response = self.client.post(reverse("post_edit", args="1"), {
            "title": "Updated title",
            "body": "Updated text"
        })
        self.assertEqual(response.status_code, 302)

    # We test our delete view by confirming that if we delete a post, the status code is 302, a redirect since the item no longer exists
    def test_post_delete_view(self):
        response = self.client.post(reverse("post_delete", args="1"))
        self.assertEqual(response.status_code, 302)
