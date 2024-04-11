from django.db import models
from django.contrib.auth.models import AbstractUser,Group

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True
        

class UserGroup(BaseModel):
    name = models.CharField(max_length=32)

    def save(self,*args,**kwargs):
        '''
        get or create group with name
        '''
        group, created = Group.objects.get_or_create(name = self.name)
        return super().save(*args,**kwargs)
    

class User(AbstractUser, BaseModel):
    display_name = models.CharField(max_length = 32, db_index= True)






