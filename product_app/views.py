from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from rest_framework.routers import DefaultRouter

from product_app.models import Product
from product_app.serializers import ProductSerializer
from product_app.permissions import AllowAdminOnly


class ProductViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin,\
                     mixins.UpdateModelMixin, GenericViewSet):
    '''
    Viewset for Product model
    '''
    queryset = Product.objects.all()     # retreiving all objects of product model 
    serializer_class = ProductSerializer  
    permission_classes = [IsAuthenticated]  #setting permission types for this view



    def get_permissions(self):
        if self.request.method.upper() in ['HEAD', 'OPTIONS']: #allow all users
            return []
        if self.request.method.upper() in ['GET','POST']: #only authenticated users
            return [IsAuthenticated()]
        if self.request.method.upper() in ['PATCH', 'PUT', 'DELETE']:  # allow only admin
            return [AllowAdminOnly()]
    
    def get_serializer_class(self):
        return super().get_serializer_class() 

router = DefaultRouter()
router.register("product", ProductViewSet, "product")