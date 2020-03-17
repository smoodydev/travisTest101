"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# add some libraries, i.e. So we're going to take the include library, which allows us to include extra URL files, which we'll want to do.

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import Redirectview
from django.views.static import serve
from .settings import MEDIA_ROOT

# the carrot (^) is for the beginning of a line and the carrot ($) for the end

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # below So in effect, this is our root directory. And if somebody goes to the root directory of our project, then we want to redirect them to posts.
    url(r'^$', Redirectview.as_view(url='posts/')),
    # Okay, for our next URL then, if somebody goes to the posts URL, then we want it to be passed using the URLs in the urls.py file in the posts app
    url(r'posts/', include('posts.urls')),
    # NO IDEA the following regular expression code does
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]




