from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    url(r'^$', views.Search.as_view(), name='chatalert_search'),
    url(r'^json/$', views.SearchJSON.as_view(), name='chatalert_search_json'),
    url(r'^(?P<pk>\d+)/edit/$',
        csrf_exempt(views.SearchEdit.as_view()),
        name='chatalert_search_edit'),
]
