from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Pizza(models.Model):
    sno = models.AutoField(primary_key=True)
    Pizza_name = models.CharField(max_length=100)
    Pizza_desc = models.TextField()
    Pizza_price = models.FloatField()
    image_url = models.URLField(default="")
    
    def __str__(self):
        return self.Pizza_name
    
class Orders(models.Model):
    Pizza_name = models.CharField(max_length=100)
    Pizza_desc = models.TextField()
    Pizza_price = models.FloatField()
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    order_confirmed = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.Pizza_name
    

class Profile(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True )
    profile_Image = models.ImageField(upload_to="images", default="image/defaultuser.png", blank=True, null=True)
    def __str__(self):
        return self.User.username
     
class Address(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True )
    address = models.CharField(max_length=150)
    
    def __str__(self):
        return self.User.username

class Contact(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True )
    query = models.TextField()
    
    def __str__(self):
        return self.User.username
    