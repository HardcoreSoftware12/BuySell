from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length =255)

    class Meta:
        ordering = ('name',)#for ascending order of cat's
        verbose_name_plural = "Categories"  #to avoid Categorys


    def __str__(self):
        return self.name # to get the exact names not Onject1 etc



class Item(models.Model):

    category = models.ForeignKey(Category,related_name="items",on_delete=models.CASCADE)#id cat is dltd items are dleted

    name=models.CharField(max_length = 255)
    description = models.TextField(blank=True,null=True)
    price= models.FloatField()
    image = models.ImageField(upload_to="item_images",blank=True,null=True)
    is_sold = models.BooleanField(default=False)

    created_by = models.ForeignKey(User,related_name="items",on_delete= models.CASCADE)#user is dltd after no item i guess

    created_at = models.DateTimeField(auto_now_add=True)


    
    def __str__(self):
        return self.name # to get the exact names not Onject1 etc