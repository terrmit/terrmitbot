from django.conf.urls import url
from django.contrib import admin

from .views import CommandReceiveView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bot/(?P<bot_token>.+)/?$', CommandReceiveView.as_view(), name='command'),
]
