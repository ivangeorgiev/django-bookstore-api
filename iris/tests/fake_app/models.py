from django.db import models
from iris import fields

class Order(models.Model):
    id = models.AutoField(primary_key=True)

class OrderItem(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    sequential_number = fields.SequentialNumberField(key="order", start_at=11, increment=5)
