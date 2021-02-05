from django.urls import path
from .views import BlogListView

urlpatterns = [
    # The empty string tells python to match all values
    path("", BlogListView.as_view(), name="home"),
    
]