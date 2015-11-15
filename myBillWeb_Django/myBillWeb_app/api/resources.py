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
    authorization = DjangoAuthorization()
    authentication=BasicAuthentication()
    excludes = ['email', 'password', 'is_superuser']
    filtering = { 
        'username':ALL_WITH_RELATIONS, 
        }

  def apply_authorization_limits(self, request, object_list):
    return object_list.filter(user=request.user)

class CategoryResource(ModelResource):
  user=fields.ForeignKey(UserResource, 'username',null=False)
  class Meta:
    queryset = Category.objects.all()
    authorization = DjangoAuthorization()
    authentication=BasicAuthentication()
    allowed_methods = ['get', 'post', 'put', 'delete']
    detail_allowed_methods = ['get', 'post', 'put', 'delete']
    filtering = {
                'id':ALL,
                'user':ALL_WITH_RELATIONS
                }
  def apply_authorization_limits(self, request, object_list):
    return object_list.filter(user=request.user)

class CompanyResource(ModelResource):
  category=fields.ForeignKey(CategoryResource, 'category',full=True)
  user=fields.ForeignKey(UserResource, 'username',null=False)
  class Meta:
    queryset = Company.objects.all()
    authorization = DjangoAuthorization()
    authentication=BasicAuthentication()
    allowed_methods = ['get', 'post', 'put', 'delete']
    detail_allowed_methods = ['get', 'post', 'put', 'delete']
    filtering = {
                'id':ALL,
                'category':ALL_WITH_RELATIONS,
                'user':ALL_WITH_RELATIONS
                }
  def apply_authorization_limits(self, request, object_list):
    return object_list.filter(user=request.user)

class RecordResource(ModelResource):
  company=fields.ForeignKey(CompanyResource, 'company',full=True)
  user=fields.ForeignKey(UserResource, 'username',null=False)
  class Meta:
    queryset = Record.objects.all()
    authorization = DjangoAuthorization()
    authentication=BasicAuthentication()
    allowed_methods = ['get', 'post', 'put', 'delete']
    detail_allowed_methods = ['get', 'post', 'put', 'delete']
    filtering = {
                'id':ALL_WITH_RELATIONS,
                'company':ALL_WITH_RELATIONS,
                'user':ALL_WITH_RELATIONS
                }
  def apply_authorization_limits(self, request, object_list):
    return object_list.filter(user=request.user)
