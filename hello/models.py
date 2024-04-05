from django.db import models
import uuid

# Create your models here.
class FarmingEquipment(models.Model):
  name = models.CharField(max_length=255, unique=True)  # Enforces unique product names
  image = models.ImageField(upload_to='hello/images')
  description = models.TextField()  # Allows for longer descriptions
  price = models.DecimalField(max_digits=10, decimal_places=2)

  def __str__(self):
    return self.name


