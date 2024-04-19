from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.routers import DefaultRouter
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from product_app.models import Product
from product_app.serializers import ProductSerializer
from product_app.permissions import AllowAdminOnly


class ProductViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,\
                     mixins.UpdateModelMixin, GenericViewSet):
    '''
    Viewset for Product model
    '''
    # retreiving all objects of product model 
    queryset = Product.objects.all()    
    
    serializer_class = ProductSerializer
    # setting permission types for this view set 
    permission_classes = [IsAuthenticated] 
    # setting fiter backend
    filter_backends = [DjangoFilterBackend]
    #adding fields to filterset class which enables queries from request url
    filterset_fields = ['name','category']

    ordering_fields = ['name','category','price','mfg_date']
    search_fields = ['name','category']







    def get_permissions(self):
        if self.request.method.upper() in SAFE_METHODS: #allow all users
            return []
        if self.request.method.upper() in ['POST']: #only authenticated users
            return [IsAuthenticated()]
        if self.request.method.upper() in ['PATCH', 'PUT', 'DELETE']:  # allow only admin
            return [AllowAdminOnly()]
    
    def get_serializer_class(self):
        return super().get_serializer_class() 



router = DefaultRouter()
router.register("product", ProductViewSet, "product")