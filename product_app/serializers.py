<<<<<<< HEAD
from rest_framework.serializers import ModelSerializer

from product_app.models import Product

class BaseSerializer(ModelSerializer):
    '''
    Base serializer for all product_app serializers
    '''
    class Meta:
        fields = ['id', 'created_at', 'updated_at']
        fields_read_only = ['id', 'created_at', 'updated_at']


class ProductSerializer(BaseSerializer):
    '''
    Serializer method for Product model
    '''
    class Meta:
        model = Product
        # all fields of model are included
        fields = '__all__'  
=======
from rest_framework.serializers import ModelSerializer

from product_app.models import Product

class BaseSerializer(ModelSerializer):
    '''
    Base serializer for all product_app serializers
    '''
    class Meta:
        fields = ['id', 'created_at', 'updated_at']
        fields_read_only = ['id', 'created_at', 'updated_at']


class ProductSerializer(BaseSerializer):
    '''
    Serializer method for Product model
    '''
    class Meta:
        model = Product
        fields = '__all__'  #all fields of model are included
>>>>>>> a4e0b28050ba90bcdb878c286b5351ddc1496045
