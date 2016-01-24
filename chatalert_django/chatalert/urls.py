from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Search.as_view(), name='chatalert_search'),
    url(r'^json/$', views.SearchJSON.as_view(), name='chatalert_search_json'),
]
