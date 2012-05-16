from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
admin.autodiscover()

from api.resources import UserResource
from api.resources import PublicSessionResource
from api.resources import InvitationResource
from api.resources import IdeaResource

swm_api = Api(api_name='v1')
swm_api.register(UserResource())
swm_api.register(PublicSessionResource())
swm_api.register(InvitationResource())
swm_api.register(IdeaResource())

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(swm_api.urls)),
    url(r'^/?$', 'web.views.home'),
    url(r'^web/', include('web.urls')),
    
    # jasmine testings urls
    url(r'^jasmine/', include('django_jasmine.urls')),
)
