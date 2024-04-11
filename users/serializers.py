from rest_framework import serializers
from django.contrib.auth.hashers import make_password

from  users.models import User,UserGroup

class BaseSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','created_at','updated_at']
        fields_read_only = ['id','created_at','updated_at']

class UserSerializer(BaseSerializer):
    class Meta:
        model = User
        fields = '__all__'  
        extra_kwargs = {
            'password':{'write_only':True}
        } 

    def validate(self,attrs):
        #attrs contains dictionary of attributes provided from Http request methods
        password = attrs['password'] #getting value of key - password 

        if password is not None:
            attrs['password']  = make_password(password)#hashing password
            return super().validate(attrs)

        
            
class UserGroupSerializer(BaseSerializer):
    '''
    Serializer for User group model
    '''
    class Meta:
        model = UserGroup
        fields = BaseSerializer.Meta.fields + ['name']
