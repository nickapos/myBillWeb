# -*- coding: utf-8
import sys
import os
from datetime import datetime 
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class Category(models.Model):
 '''The class will describe the categories of companies
 '''
 categoryName = models.CharField(_('Category name'),max_length=200)
 add_date = models.DateField(_('date added'),default=datetime.now, blank=True)
 username=models.ForeignKey(User)
 comment = models.CharField(_('Comment'),max_length=200)
 checksum = models.CharField(_('Checksum'),max_length=200)
 #create a unique constraint. the category name will be unique per user
 class Meta:
    unique_together = ('username', 'categoryName',)
 def __unicode__(self):
   return self.username.username+' '+self.categoryName
 def description(self):
   return self.categoryName
 def getId(self):
  return self.id
 def getName(self):
  return self.categoryName
 def getDate(self):
  return self.add_date
 def getUsername(self):
  return self.username
 def getComment(self):
  return self.comment
 def getChecksum(self):
  return self.checksum
 def checkOwnership(self,id):
  ''' this function will be used by to verify that the incoming owner id is the 
  owner of this specific object
  '''
  if self.username.id==id:
   return True
  return False


class Company(models.Model):
 '''The class will describe the companies
 '''
 companyName = models.CharField(_('Company name'),max_length=200)
 category = models.ForeignKey(Category)
 add_date = models.DateField(_('date added'),default=datetime.now, blank=True)
 username=models.ForeignKey(User)
 comment = models.CharField(_('Comment'),max_length=200)
 checksum = models.CharField(_('Checksum'),max_length=200)
 def __unicode__(self):
   return self.username.username+' '+self.companyName
 def description(self):
   return self.companyName
 def getId(self):
  return self.id
 def getName(self):
  return self.companyName
 def getDate(self):
  return self.add_date
 def getCategory(self):
  return self.category
 def getComment(self):
  return self.comment
 def getUsername(self):
  return self.username
 def getChecksum(self):
  return self.checksum
 def checkOwnership(self,id):
  ''' this function will be used by to verify that the incoming owner id is the 
  owner of this specific object
  '''
  if self.username.id==id:
   return True
  return False


class Record(models.Model):
 '''The class will describe the flow records
  the same class will represent both income and expenses
 '''
 EXPENSES='EX'
 INCOME='IN'
 TYPE_OF_RECORDS=(
     (EXPENSES,'Expenses'),
     (INCOME,'Income')
     )
 company = models.ForeignKey(Company)
 issue_date = models.DateField(_('issue date'),default=datetime.now, blank=True)
 pay_date = models.DateField(_('pay date'),default=datetime.now, blank=True)
 username=models.ForeignKey(User)
 comment = models.CharField(_('Comment'),max_length=200,default=' ',null=True, blank=True)
 mybillId = models.IntegerField(_('myBillDesktopId'),default=-1)
 amount=models.FloatField(_('Amount'),default=0.0)
 checksum = models.CharField(_('Checksum'),max_length=200)
 type_of_record = models.CharField(max_length=2,
                                      choices=TYPE_OF_RECORDS,
                                      default=EXPENSES)
 def __unicode__(self):
  return "".join([str(self.getAmount()),' - ',self.company.getName(),' ',unicode(self.getPayDate()).encode("utf-8"),' ',self.comment.encode("utf-8"),' (',self.getTypeOfRecord(),')']) 
 def description(self):
  return "".join([str(self.getAmount()),' - ',self.company.getName(),' ',unicode(self.getPayDate()).encode("utf-8"),' ',self.comment.encode("utf-8"),' (',self.getTypeOfRecord(),')']) 
 def getId(self):
  return self.id
 def getName(self):
  return "".join([str(self.getAmount()),' - ',self.company.getName(),' ',unicode(self.getPayDate()).encode("utf-8"),' ',self.comment.encode("utf-8"),' (',self.getTypeOfRecord(),')']) 
 def getIssueDate(self):
  return self.issue_date
 def getPayDate(self):
  return self.pay_date
 def getCategory(self):
  return self.category
 def getComment(self):
  return self.comment
 def getUsername(self):
  return self.username
 def getChecksum(self):
  return self.checksum
 def getAmount(self):
  return self.amount
 def getTypeOfRecord(self):
  return self.type_of_record
 def checkOwnership(self,id):
  ''' this function will be used by to verify that the incoming owner id is the 
  owner of this specific object
  '''
  if self.username.id==id:
   return True
  return False
