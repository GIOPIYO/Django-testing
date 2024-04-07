from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FarmingEquipment(models.Model):
  name = models.CharField(max_length=255, unique=True)  # Enforces unique product names
  image = models.ImageField(upload_to='hello/images')
  description = models.TextField()  # Allows for longer descriptions
  price = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(FarmingEquipment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in cart"