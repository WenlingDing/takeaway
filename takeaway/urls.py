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
from cart import urls as urls_food
from django.conf.urls.static import static
from accounts import urls as accounts_url
from takeaway_app.views import  food_detail, search, index,menu
from checkout import urls as urls_checkout
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index,name='index'),
    url(r'^user/', include(accounts_url.urlpatterns)),
	url(r'^search/$', search, name='search'),
	url(r'^menu/(?P<id>\d+)$', menu, name='menu'),
	url(r'detail/(?P<id>\d+)$', food_detail, name='food_detail'),
	url(r'^cart/', include(urls_food.urlpatterns)),
	url(r'^checkout/', include(urls_checkout)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)