from django.contrib.auth.models import User
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource,Resource
from myBillWeb_app.models import Category, Company, Record
from tastypie.resources import ModelResource,ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization


class UserResource(ModelResource):
  class Meta:
    queryset = User.objects.all()
    resource_name = 'auth/user'
    excludes = ['email', 'password', 'is_superuser']

class CategoryResource(ModelResource):
  class Meta:
    queryset = Category.objects.all()
    authorization = DjangoAuthorization()
    allowed_methods = ['get']
    filtering = {
                'id':ALL,
                'user':ALL_WITH_RELATIONS
                }

class CompanyResource(ModelResource):
  category=fields.ForeignKey(CategoryResource, 'category',full=True)
  class Meta:
    queryset = Company.objects.all()
    authorization = DjangoAuthorization()
    allowed_methods = ['get']
    filtering = {
                'id':ALL,
                'category':ALL_WITH_RELATIONS,
                'user':ALL_WITH_RELATIONS
                }

class RecordResource(ModelResource):
  company=fields.ForeignKey(CompanyResource, 'company',full=True)
  class Meta:
    queryset = Record.objects.all()
    authorization = DjangoAuthorization()
    allowed_methods = ['get']
    filtering = {
                'id':ALL_WITH_RELATIONS,
                'company':ALL_WITH_RELATIONS,
                'user':ALL_WITH_RELATIONS
                }
