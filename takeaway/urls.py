"""takeaway URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static
from accounts import urls as accounts_url
from takeaway_app.views import index,menu,food, food_detail,search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include(accounts_url.urlpatterns)),
    url(r'^$', index),
	url(r'^menu/(?P<menu_name>\w+)/$', menu, name='menu'),
	url(r'^food/(?P<food_name>\w+)/$', food, name='food'),
	url(r'^search/$', search, name='search'),
	url(r'^more/(?P<menu_name>\w+)/$', food_detail)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)