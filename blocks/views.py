# -*- coding: utf-8  -*-
from django.shortcuts import render, get_object_or_404
from .models import Book,Comment
from django.views import generic
from .forms import BookForm,CommentForm
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy

class IndexView(generic.ListView):
    template_name = 'blocks/index.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.all()

def show_index(request):
    pass
class DetailView(generic.DetailView):
    model = Book
    template_name = 'blocks/detail.html'

class BookCreate(CreateView):
    model = Book
    fields = ['title','description','cover','download']

class BookUpdate(UpdateView):
    model = Book
    fields = ['title','description','cover','download']

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('m9adery:books')

class CommentCreate(CreateView):
    model = Comment
    fields = ['description']

# #def detail(request,book_id):
#     book = get_object_or_404(Book,pk=book_id)
#     form = CommentForm(request.POST or None)
#     context = {'form': form,
#                'book':book}
#     if form.is_valid():
#         form.save()
#     return render(request, 'blocks/detail.html', context)
'''def index(request):
    all_books = Book.objects.all()
    form = BookForm(request.POST)
    context = {
        'all_books':all_books,
        'form':form
    }
    if form.is_valid():
        form.save()
    return render(request, 'blocks/index.html', context)'''