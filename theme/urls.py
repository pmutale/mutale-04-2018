from django.conf.urls import url

from theme.views import Theme
app_name = 'theme'

urlpatterns = [
    url('^theme/', Theme.as_view(), name='index'),
    url('^login/', Theme.as_view(), name='login'),
]