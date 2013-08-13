from django.conf.urls import patterns, url

urlpatterns = patterns('rename_this_app.views',
    url(r'^$', 'index', name='index'),
)
