# Create your views here.
# CRUD : Create, Read, Update, Delete
# List

# view : class(generic view), function(when you want to do something)
# access webpage -> see the webpage
# input URL -> Server looks for View -> Response
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView) :
    model = Bookmark

class BookmarkCreateView(CreateView):
    model = Bookmark
    # ImproperlyConfigured at /myapp/add/ : Fields are needed
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_edit'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
