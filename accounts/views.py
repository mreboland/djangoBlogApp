# UserCreationForm provides us an easy to use form that by default provides us three fields. Username, password1, and password2.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# We are subclassing the generic class-based view CreateView in our SignUpView class.
class SignUpView(generic.CreateView):
    # Specifying the use of the built-in UserCreationForm and the template at signup.html
    form_class = UserCreationForm
    # We use reverse_lazy to redirect the user to the log in page upon successful registration.
    # We use the lazy vs just reverse because for all generic class-based views, the URLs are not loaded when the file is imported. So to load them we need to use the lazy form of reverse when they are available.
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"