
from django.conf.urls import url
from . import views
from shopdb.settings import MEDIA_ROOT, DEBUG
from django.conf.urls.static import static
from django.conf import settings
from shop.views import FlowerDelete



urlpatterns = [

    url(r'^$', views.main_page, name='main'),
    url(r'^dodaty_kvitku', views.flower_add, name='flower_add'),
    url(r'^flower/(?P<pk>\d+)/one/', views.one_flower, 
    	name='one_flower'),
    url(r'^redahuvaty/(?P<pk>\d+)/kvitku', views.flower_edit,
    	name='flower_edit'),
    url(r'^vydalyty/(?P<pk>\d+)/kvitku', FlowerDelete.as_view(),
        name='flower_del'),
    url(r'^search', views.search, name='search'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)