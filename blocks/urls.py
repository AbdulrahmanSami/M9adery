from django.conf.urls import url
from . import views
from django.views.generic.base import RedirectView
app_name= 'm9adery'
urlpatterns = [
    url(r'^$',views.show_index,name='index'),
    url(r'^books/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    #url(r'^books/$',views.IndexView.as_view(),name='books'), doesn't work?
    #/m9adery/books/add/
    #url(r'^books/(?P<book_id>[0-9]+)/edit$', views.editbook, name='editbook'),
    url(r'^books/$', views.index,name='books'),
]