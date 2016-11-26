from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Profile,Book,Block,College,Comment,CommentRating
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields =['title','description','cover','download',]
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields =['description']