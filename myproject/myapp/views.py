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
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
class BookmarkListView(ListView) :
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    # ImproperlyConfigured at /myapp/add/ : Fields are needed
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'