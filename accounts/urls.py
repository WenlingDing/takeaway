from django.conf.urls import url
from accounts.views import logout, login, register

urlpatterns = [
    url(r'logout/$', logout, name="logout_link"),
    url(r'login/$', login, name="login_link"),
    url(r'register/$', register, name="register_link"),
]
