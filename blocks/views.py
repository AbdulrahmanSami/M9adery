# -*- coding: utf-8  -*-
from django.shortcuts import render, get_object_or_404
from .models import Book,Comment,Block,Category
from django.views import generic
from .forms import BookForm,CommentForm,CategoryForm
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect

class IndexView(generic.ListView):
    template_name = 'blocks/index.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.all()
class IndexHomeView(generic.ListView):
    template_name = 'blocks/homepage.html'
    context_object_name = 'all_blocks'

    def get_queryset(self):
        return Block.objects.all()

def show_index(request):
    pass
def ao22(request):
    pass
class DetailView(generic.DetailView):
    model = Book
    template_name = 'blocks/detail.html'
class BlockDetailView(generic.DetailView):
    model = Block
    template_name = 'blocks/blockcategories.html'
class CategoryDetailView(generic.DetailView):
    model = Block
    template_name = 'blocks/categorybooks.html'
def show_category(request,block_pk,category_pk):
    block = get_object_or_404(Block,pk=block_pk)
    category = get_object_or_404(Category,pk=category_pk)
    books= Book.objects.filter(block=block,category=category)
    context = {'books':books,
              'category':category,
               'block':block}
    return render(request,'blocks/categorybooks.html',context)
class BookCreate(CreateView):
    model = Book
    fields = ['title','description','cover','download','category','block']
class CategoryCreate(CreateView):
    model = Category
    fields = ['name','cover','block']

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
def add_comment(request,pk):
    book = get_object_or_404(Book, pk=pk)
    # PERMISSION CHECK
    #if not request.user.is_superuser  and \
        #not request.user == book.submitter:
        #raise PermissionDenied


    if request.method == "GET":
        form = CommentForm()
    elif request.method == "POST":
        instance = Comment(books=book, submitter=request.user)
        form = CommentForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('m9adery:detail', args=(pk,)))
    context = {
        'form':form
    }

    return render(request, 'blocks/comment_form.html', context)
def add_category(request,pk):
    block = get_object_or_404(Block, pk=pk)
    if request.method == "GET":
        form = CategoryForm()
    elif request.method == "POST":
        instance = Category(block=block, submitter=request.user)
        form = CategoryForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('m9adery:blockdetail', args=(pk,)))
    context = {
        'form':form
    }

    return render(request, 'blocks/category_form.html', context)