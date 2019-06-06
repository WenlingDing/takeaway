from django.conf.urls import url
from accounts.views import logout, login, register,index

urlpatterns = [
    url(r'^$', index),
    url(r'logout/$', logout, name="logout_link"),
    url(r'login/$', login, name="login_link"),
    url(r'register/$', register, name="register_link"),
]
