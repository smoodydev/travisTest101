from django.conf.urls import urls
from .views import get_posts, post_detail, create_or_edit_post

urlpatterns = [
    # root directory for the posts app
    url(r'^$', get_posts, name='get_posts')
    # 
    url(r'^(?P<pk>\d+)/$', post_detail, Name=post_detail)
    url(r'^new/$', create_or_edit_post, Name=new_post)
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, Name=edit_post)
]
