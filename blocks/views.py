# -*- coding: utf-8  -*-
from django.shortcuts import render, get_object_or_404
from .models import Book
from django.views.generic.edit import CreateView,DeleteView,UpdateView
def index(request):
    all_books = Book.objects.all()
    context = {
        'all_books':all_books,
    }
    return render(request, 'blocks/index.html', context)

def show_index(request):
    pass
def detail(request,book_id):
    book = get_object_or_404(Book,pk=book_id)
    return render(request, 'blocks/detail.html', {'book':book,})
