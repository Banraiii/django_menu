from django.conf.urls import url
from .views import IndexView
# from menus.views import menu_item

app_name = 'multitree'

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(.*)/$', IndexView.as_view(), name='index'),
]
