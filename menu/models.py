from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Menu(models.Model):
    item=models.CharField(max_length=250)
    price=models.IntegerField()
    image=models.ImageField(upload_to='food/images/')
    description=models.CharField(max_length=250)
    calories=models.IntegerField()

    def __str__(self):
        return self.item

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user}, Product: {self.product}"
    

