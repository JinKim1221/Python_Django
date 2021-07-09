from django.urls import path
from django.urls.resolvers import URLPattern
from .views import BookmarkListView

urlpatterns = [
    # http://127.0.0.1/myapp/????
    # ?????
    path("", BookmarkListView.as_view(), name='List'),
]