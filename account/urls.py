from django.conf.urls import url, include
# from django.contrib.auth.views import login, logout, \
#     logout_then_login, password_change, password_change_done, \
#     password_reset, password_reset_done, password_reset_confirm, \
#     password_reset_complete
from . import views


app_name = 'account'
urlpatterns = [
    # previous login view
    # url(r'^login/$', views.user_login, name='login'),

    url(r'^$', views.dashboard, name='dashboard'),

    # login / logout urls
    # ya no sirve la forma 'django.contrib.auth.views.login',
    # ahora se tiene que importar todo
    # url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    # url(r'^logout-then-login/$',
    # 'django.contrib.auth.views.logout_then_login',
    # name='logout_then_login'),
    # url(r'^login/$', login, name='login'),
    # url(r'^logout/$', logout, name='logout'),
    # url(r'^logout-then-login/$', logout_then_login,
    #     name='logout_then_login'),

    # # Change passwords
    # url(r'^password-change/$', password_change, name='password_change'),
    # url(r'^password-change/done/$', password_change_done,
    #     name='password_change_done'),
    # # restore password urls
    # url(r'^password-reset/$', password_reset, name='password_reset')
    # url(r'^password-reset/done/$', password_reset_done,
    #     name='password_reset_done'),
    # url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
    #     password_reset_confirm, name='password_reset_confirm'),
    # url(r'^password-reset/complete/$', password_reset_complete,
    #     name='password_reset_complete'),
    url('^', include('django.contrib.auth.urls')),
    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),
]
