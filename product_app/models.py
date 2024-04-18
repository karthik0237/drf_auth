<<<<<<< HEAD
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


class Product(BaseModel):
    name = models.CharField(max_length=32, db_index = True)
    category = models.CharField(default = "All", max_length=32)
    mfg_date = models.DateField(default=None)
    price = models.FloatField(null = False)



=======
from django.db import models

# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True


class Product(BaseModel):
    name = models.CharField(max_length=32, db_index = True)
    category = models.CharField(default = "All", max_length=32)
    mfg_date = models.DateField(default=None)
    price = models.FloatField(null = False)



>>>>>>> a4e0b28050ba90bcdb878c286b5351ddc1496045
