<<<<<<< HEAD
from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,\
                                    RetrieveModelMixin,DestroyModelMixin
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import SAFE_METHODS

from users.models import User,UserGroup
from users.serializers import UserSerializer,UserGroupSerializer
from rest_framework.permissions import IsAuthenticated
from product_app.permissions import AllowAdminOnly


# Create your views here.
class UserViewset(ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,\
                  DestroyModelMixin,GenericViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.request.method.upper() in SAFE_METHODS :
            return []
        if self.request.method.upper() in ['POST']:
            return [IsAuthenticated()]
        if self.request.method.upper() in ['PATCH','PUT','DELETE']:
            return [AllowAdminOnly()]
    
    def get_serializer_class(self):
        return super().get_serializer_class()

        


class UserGroupViewset(ListModelMixin, CreateModelMixin, \
                       RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    '''
    Viewset for UserGroup Model
    '''
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer
    
    def get_permissions(self):
        if self.request.method.upper() in SAFE_METHODS:
            return []
        if self.request.method.upper() in ['POST','PUT','DELETE','PATCH']:
            return [AllowAdminOnly()]
        
    def get_serializer_class(self):
        return super().get_serializer_class()
        



router = DefaultRouter()
router.register("users",UserViewset)
router.register("groups", UserGroupViewset, "group")


=======
from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,\
                                    RetrieveModelMixin,DestroyModelMixin
from rest_framework.routers import DefaultRouter

from users.models import User,UserGroup
from users.serializers import UserSerializer,UserGroupSerializer
from product_app.permissions import AllowAdminOnly


# Create your views here.
class UserViewset(ListModelMixin,CreateModelMixin,UpdateModelMixin,RetrieveModelMixin,\
                  DestroyModelMixin,GenericViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserGroupViewset(ListModelMixin, CreateModelMixin, \
                       RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    '''
    Viewset for UserGroup Model
    '''
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer
    
    def get_permissions(self):
        if self.request.method.upper() in ['HEAD','GET','OPTIONS']:
            return []
        if self.request.method.upper() in ['PUT','POST','DELETE','PATCH']:
            return [AllowAdminOnly()]
        
    def get_serializer_class(self):
        return super().get_serializer_class()
        



router = DefaultRouter()
router.register("users",UserViewset)
router.register("groups", UserGroupViewset, "group")


>>>>>>> a4e0b28050ba90bcdb878c286b5351ddc1496045
