from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField('法人名', max_length=255)
    representative_name = models.CharField('代表者名', max_length=255)
    company_number = models.CharField('法人番号',max_length=255, unique=True)
    address = models.CharField('住所', max_length=255)
    phone_number = models.CharField('電話番号',max_length=255,blank=True)

    created_at = models.DateTimeField('登録日',auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.name

