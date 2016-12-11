from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile,Book,Block,College,Comment,CommentRating,Category
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['submitter', 'category']
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields =['description']
class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name','block','cover']