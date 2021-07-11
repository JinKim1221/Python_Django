from django.urls import path
from .views import *

urlpatterns = [
    # http://127.0.0.1/myapp/????
    # ?????
    path("", BookmarkListView.as_view(), name='list'),
    path("add/", BookmarkCreateView.as_view(), name="add"),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name="detail"),
    #<int:pk> : primary key of each bookmark
    path("edit/<int:pk>/", BookmarkUpdateView.as_view(), name = "edit"),
]   