# -*- coding: utf-8
import sys
import os
from django.db import models
from django.contrib.auth.models import User
sys.setdefaultencoding( "utf-8" )
# Create your models here.


class Category(models.Model):
 '''The class will describe the categories of companies
 '''
 categoryName = models.CharField(_('Category name'),max_length=200)
 add_date = models.DateField(_('date added'))
 username=models.ForeignKey(User)
 comment = models.CharField(_('Comment'),max_length=200)
 #create a unique constraint. the category name will be unique per user
 class Meta:
    unique_together = (self.username.id, 'categoryName',)
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
 def getComment(self):
  return self.comment
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
 add_date = models.DateField(_('date added'))
 username=models.ForeignKey(User)
 comment = models.CharField(_('Comment'),max_length=200)
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
 add_date = models.DateField(_('date added'))
 username=models.ForeignKey(User)
 comment = models.CharField(_('Comment'),max_length=200)
 checksum = models.CharField(_('Checksum'),max_length=200)
 type_of_record = models.CharField(max_length=2,
                                      choices=TYPE_OF_RECORDS,
                                      default=EXPENSES)
 def __unicode__(self):
  return "".join([self.company.getName(),' ',self.getDate(),' ',self.comment.encode("utf-8")]) 
 def description(self):
  return "".join([self.company.getName(),' ',self.getDate(),' ',self.comment.encode("utf-8")]) 
 def getId(self):
  return self.id
 def getName(self):
  return "".join([self.company.getName(),' ',self.getDate(),' ',self.comment.encode("utf-8")]) 
 def getDate(self):
  return self.add_date
 def getCategory(self):
  return self.category
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
