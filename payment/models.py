from django.db import models
from django.contrib.auth.models import User
from selection.models import Orders

# Create your models here.
class OrderHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_p')
    orderdate = models.DateTimeField()
    deliverydate = models.DateTimeField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    order = models.ManyToManyField(Orders, related_name='order_p')
    def __str__(self):
        return str(self.user.username)

    def orderlist(self):
        return ",".join([str(p) for p in self.order.all()])

