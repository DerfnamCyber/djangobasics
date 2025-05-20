from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(max_digits=10000, decimal_places=2)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField(default=True)
    
    #Dynamic url linking
    #def get_absolute_url(self):
     #   return f"/products/{self.id}/"
    
    #Django dynamic url reverse
    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id})
        
    
    
    

"""
max_length = required

#blank=False == Makes the field required,
Blank : How the field is rendered
Null : The Datebase

"""