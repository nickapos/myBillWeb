from tastypie.resources import ModelResource,Resource
from myBillWeb_app.models import Category, Company, Record
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization

class CategoryResource(ModelResource):
  class Meta:
    queryset = Category.objects.all()
    allowed_methods = ['get']
    filtering = {
                'id':ALL_WITH_RELATIONS,
                }

class CompanyResource(ModelResource):
  category=fields.ForeignKey(CategoryResource, 'category',full=True)
  class Meta:
    queryset = Company.objects.all()
    allowed_methods = ['get']
    filtering = {
                'id':ALL_WITH_RELATIONS,
                'category':ALL_WITH_RELATIONS,
                }

class RecordResource(ModelResource):
  company=fields.ForeignKey(CategoryResource, 'company',full=True)
  class Meta:
    queryset = Record.objects.all()
    allowed_methods = ['get']
    filtering = {
                'id':ALL_WITH_RELATIONS,
                }
