from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView
app_name= 'm9adery'
urlpatterns = [
    url(r'^$',views.show_index,name='index'),
    url(r'^books/(?P<book_id>[0-9]+)/$',views.detail,name='detail'),
    #/m9adery/books/add/
    url(r'book/add/$', views.BookCreate.as_view(), name='book-add'),
    url(r'^userprofile/',views.show_index,name='user profile'),
    url(r'^block',views.show_index,name='books'),
    url(r'^books/$', views.index,name='books'),
    url(r'^newbook',views.show_index,name='add a new book')
]