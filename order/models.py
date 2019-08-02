from django.db import models
from django.contrib.auth.models import User
from selection.models import Collar, ClothMenu, Cuff, Back, Pocket, Front, Measurement, StandardSize
# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_o')
    cloth_menu = models.ForeignKey(ClothMenu, on_delete=models.CASCADE, related_name='clothmenu_o')
    collar = models.ForeignKey(Collar, on_delete=models.CASCADE, related_name='collar_o')
    cuff = models.ForeignKey(Cuff, on_delete=models.CASCADE, related_name='cuff_o')
    back = models.ForeignKey(Back, on_delete=models.CASCADE, related_name='back_o')
    pocket = models.ForeignKey(Pocket, on_delete=models.CASCADE, related_name='pocket_o')
    front = models.ForeignKey(Front, on_delete=models.CASCADE, related_name='front_o')
    size = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='Measurement_o', null=True, blank=True)
    standard_size = models.ForeignKey(StandardSize, on_delete=models.CASCADE, related_name='standardsize_o', null=True, blank=True)
    confirm = models.BooleanField()

    def __str__(self):
        return str(self.user.username + self.id)

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'