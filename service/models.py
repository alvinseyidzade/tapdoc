from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
# Create your models here.
class XidmatlarGroup(models.Model):
    group_name = models.CharField(max_length=128, verbose_name='Xidmət Qrup Adı',null=True, blank=True)

    def __str__(self):
        return self.group_name

class Xidmatlar(models.Model):
    service_group = models.ForeignKey(XidmatlarGroup, verbose_name='Xidmətin Adı',related_name='xidmetler', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256,blank=True,null=True)

    def __str__(self):
        return self.name



class Xidmat(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


    class MPTTMeta:

        order_insertion_by=['name']

    def __str__(self):
        return self.name


class DiaqnostikalarGroup(models.Model):
    group_name = models.CharField(max_length=128, verbose_name='Diaqnostik Xidmət Qrupun Adı',null=True, blank=True)

    def __str__(self):
        return self.group_name

class Diaqnostikalar(models.Model):
    diaqnostika_group = models.ForeignKey(DiaqnostikalarGroup, verbose_name='Diaqnostik Xidmətin Adı',related_name='diaqnostikalar', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=256,blank=True,null=True)

    def __str__(self):
        return self.name

class Diaqnostika(MPTTModel):
    name = models.CharField(max_length=50)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')


    class MPTTMeta:

        order_insertion_by=['name']

    def __str__(self):
        return self.name
