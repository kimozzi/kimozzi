from django.conf.urls import url, patterns, include
from django.contrib.auth.views import login
from accounts import views
from accounts.forms import LoginForm
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^signup/$', views.signup),
    url(r'^login/$', login, kwargs = {
        'authentication_form' : LoginForm,
    }),
    url(r'^profile/$', views.profile),
    url(r'^register_success/', ('accounts.views.register_success')),
    url(r'^confirm/(?P<activation_key>\w+)/', ('accounts.views.register_confirm')),
    url(r'^sign_up/$', views.register_user),
]