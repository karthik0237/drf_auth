from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,\
                                    RetrieveModelMixin,DestroyModelMixin
from rest_framework.routers import DefaultRouter

from users.models import User,UserGroup
from users.serializers import UserSerializer,UserGroupSerializer


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



router = DefaultRouter()
router.register("users",UserViewset)
router.register("groups", UserGroupViewset, "group")


