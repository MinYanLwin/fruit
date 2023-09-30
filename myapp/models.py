from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Fruit(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    is_avaliable=models.BooleanField(default=True)
    slug=models.SlugField(default='',null=False,db_index=True)

    def get_absolute_url(self):
        return reverse("detail",args=[self.slug])

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)

    def  __str__(self):
        return f'{self.name} is {self.price}'
