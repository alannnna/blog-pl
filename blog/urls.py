from django.conf.urls import patterns, url

from blog import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^(?P<page>\d+)/$', views.index, name="index"),
        url(r'^write/$', views.writePost, name="writePost"),
        url(r'^write/save/$', views.savePost, name="savePost"),
        url(r'^post/(?P<post_id>\d+)/$', views.postDetail, name="postDetail"),
        url(r'^post/(?P<post_id>\d+)/comment$', views.postComment, name="postComment"),
        # Needed: some kind of check for alphanumeric author names
        url(r'^author/(?P<post_author>[a-zA-Z0-9]*)/$', views.indexByAuthor, name="indexByAuthor"),
        url(r'^author/(?P<post_author>[a-zA-Z0-9]*)/(?P<page>\d+)/$', views.indexByAuthor, name="indexByAuthor")
)
