from .models import Bookmark
from django.db import models
from django.shortcuts import render

# Create your views here.
# CRUD : Create, Read, Update, Delete
# List

# view : class(generic view), function(when you want to do something)
# access webpage -> see the webpage
# input URL -> Server looks for View -> Response
from django.views.generic.list import ListView

class BookmarkListView(ListView) :
    model = Bookmark
