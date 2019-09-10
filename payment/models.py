from django.db import models
from django.contrib.auth.models import User
from selection.models import Orders

# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_p')
    date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='order_p', null=True, blank=True)
    def __str__(self):
        return str(self.user.username + ' ' + self.price)

