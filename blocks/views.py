# -*- coding: utf-8  -*-
from django.shortcuts import render, get_object_or_404
from .models import Book
from django.views import generic
from .forms import BookForm
# from django.views.generic.edit import CreateView,DeleteView,UpdateView
# from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse

'''class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.all() #for some reason it doesn't work'''
def index(request):
    all_books = Book.objects.all()
    form = BookForm(request.POST or None)
    context = {
        'all_books':all_books,
        'form':form
    }
    if form.is_valid():
        form.save()
    return render(request, 'blocks/index.html', context)

def show_index(request):
    pass
class DetailView(generic.DetailView):
    model = Book
    template_name = 'blocks/detail.html'
def add_book (request):
    pass

'''def detail(request,book_id):
    book = get_object_or_404(Book,pk=book_id)
    return render(request, 'blocks/detail.html', {'book':book,})'''
