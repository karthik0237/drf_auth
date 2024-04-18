<<<<<<< HEAD
from rest_framework.permissions import BasePermission


class AllowAdminOnly(BasePermission):
    '''
    Only Allow Admin users to access
    '''
    def has_permission(self, request, view):
        
        return request.user.groups.filter(name = "Admin")
=======
from rest_framework.permissions import BasePermission

class AllowAdminOnly(BasePermission):
    '''
    Only Allow Admin users to access
    '''
    def has_permission(self, request, view):
        
        return request.user.groups.filter(name = "admin").exists
>>>>>>> a4e0b28050ba90bcdb878c286b5351ddc1496045
