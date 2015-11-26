from tastypie.authorization import Authorization
from tastypie.exceptions import Unauthorized
 
class CustomAuthorization(Authorization):
  def read_list(self, object_list, bundle):
    # This assumes a ``QuerySet`` from ``ModelResource``.
    return object_list.filter(username=bundle.request.user)

  def read_detail(self, object_list, bundle):
   print bundle.obj.username.username
   print bundle.request.user
   # Is the requested object owned by the user?
   if str(bundle.obj.username) == str(bundle.request.user):
     return True
   else:
     raise Unauthorized("Sorry, not authorized.")

 #def create_list(self, object_list, bundle):
 #  # Assuming their auto-assigned to ``user``.
 #  return object_list

 #def create_detail(self, object_list, bundle):
 #  return bundle.obj.username == bundle.request.user

 #def update_list(self, object_list, bundle):
 #  allowed = []

 #  # Since they may not all be saved, iterate over them.
 #  for obj in object_list:
 #      if obj.username == bundle.request.user:
 #          allowed.append(obj)

 #  return allowed

 #def update_detail(self, object_list, bundle):
 #  return bundle.obj.username == bundle.request.user

 #def delete_list(self, object_list, bundle):
 #  # Sorry user, no deletes for you!
 #  raise Unauthorized("Sorry, no deletes.")

 #def delete_detail(self, object_list, bundle):
 #  raise Unauthorized("Sorry, no deletes.")

class CustomUserAuthorization(Authorization):
  def read_list(self, object_list, bundle):
    # This assumes a ``QuerySet`` from ``ModelResource``.
    return object_list.filter(username=bundle.request.user)

  def read_detail(self, object_list, bundle):
   # Is the requested object owned by the user?
   if str(bundle.obj) == str(bundle.request.user):
     return True
   else:
     raise Unauthorized("Sorry, not authorized.")

 #def create_list(self, object_list, bundle):
 #  # Assuming their auto-assigned to ``user``.
 #  return object_list

 #def create_detail(self, object_list, bundle):
 #  return bundle.obj.username == bundle.request.user

 #def update_list(self, object_list, bundle):
 #  allowed = []

 #  # Since they may not all be saved, iterate over them.
 #  for obj in object_list:
 #      if obj.username == bundle.request.user:
 #          allowed.append(obj)

 #  return allowed

 #def update_detail(self, object_list, bundle):
 #  return bundle.obj.username == bundle.request.user

 #def delete_list(self, object_list, bundle):
 #  # Sorry user, no deletes for you!
 #  raise Unauthorized("Sorry, no deletes.")

 #def delete_detail(self, object_list, bundle):
 #  raise Unauthorized("Sorry, no deletes.")
