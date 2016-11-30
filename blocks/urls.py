from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView
app_name= 'm9adery'
urlpatterns = [
    url(r'^$',views.IndexHomeView.as_view(),name='homepage'),
    url(r'^books/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^blocks/(?P<pk>[0-9]+)/$', views.BlockDetailView.as_view(), name='blockdetail'),
    url(r'^blocks/(?:(?P<block_pk>\d+)/)?category/(?P<category_pk>\d+)',views.show_category,name='categorybooks'),
    #url(r'^blocks/(?P<block_pk>\d+)/category/(?P<pk>[0-9]+)/$', views.show_category, name='categorybooks'),
    url(r'books/add/$', views.BookCreate.as_view(), name='book-add'),
    #m9adery/books/1/edit
    url(r'books/(?P<pk>[0-9]+)/edit/$', views.BookUpdate.as_view, name='book-update'),
    url(r'books/(?P<pk>[0-9]+)/confirm_delete/$', views.BookDelete.as_view(), name='book-confirm_delete'),
    url(r'books/(?P<pk>[0-9]+)/delete/$', views.BookDelete.as_view, name='book-delete'),
    url(r'books/(?P<pk>[0-9]+)/comment/add/$', views.add_comment, name='comment-add'),
    url(r'^books/$',views.IndexView.as_view(),name='books'),
    #/m9adery/books/add/
    #url(r'^books/(?P<book_id>[0-9]+)/edit$', views.editbook, name='editbook'),
    #url(r'^books/$', views.index,name='books'),
]