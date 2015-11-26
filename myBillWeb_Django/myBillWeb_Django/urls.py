from django.conf.urls import patterns, include, url
from tastypie.api import Api
from myBillWeb_app.models import Category, Company, Record
from myBillWeb_app.api.resources import CategoryResource, CompanyResource, RecordResource, UserResource
from django.contrib import admin
admin.autodiscover()

#tastypie resources
v1_api = Api(api_name='v1')
v1_api.register(CategoryResource())
v1_api.register(CompanyResource())
v1_api.register(RecordResource())
v1_api.register(UserResource())


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myBillWeb_Django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(v1_api.urls)),

)
