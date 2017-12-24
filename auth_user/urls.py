
from django.conf.urls import url, include
from . import views
from shopdb.settings import MEDIA_ROOT, DEBUG
from django.conf.urls.static import static
from django.conf import settings
from shop.views import FlowerDelete
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from registration.backends.default import views as registration_views



urlpatterns = [

    url(r'^users/profile/$', TemplateView.as_view(
        template_name='registration/profile.html'), name='profile'),
    url(r'^users/logout/$', auth_views.logout, kwargs={'next_page': 'main'}, 
    	name='auth_logout'),
    url(r'^register/complete/$', TemplateView.as_view
    	(template_name='registration/confirm_email.html'),
     name='registration_complete'),
    url(r'^users/', include('registration.backends.default.urls', 
    	namespace='users')),
    url(r'^users/activate/(?P<activation_key>\w+)/$', 
    	registration_views.ActivationView.as_view(),
        name='registration_activate'),
    url(r'^users/activate/complete/$',
       TemplateView.as_view(template_name='registration/activation_complete.html'),
       name='registration_activation_complete'),
    url(r'^users_list$', views.users_list, name='users_list'),
    url(r'^users/(?P<pk>\d+)/one/$', views.users_one, name='users_one'),
    url(r'^user/(?P<pk>\d+)/edit$', views.user_one_edit, name='user_edit'),
    url(r'^activate/complete/$', TemplateView.as_view
    	(template_name='registration/login.html'),
       name='registration_activation_complete'),
    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)