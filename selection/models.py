from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class Cuff(models.Model):
    cuff_style = models.CharField(max_length=50)
    cuff_image = models.ImageField(upload_to='pics/Cuff')

    def __str__(self):
        return self.cuff_style

class Button(models.Model):
    button_style = models.CharField(max_length=50)
    button_image = models.ImageField(upload_to='pics/Button')

    def __str__(self):
        return self.button_style

class ButtonHole(models.Model):
    button_hole_style = models.CharField(max_length=50)
    button_hole_image = models.ImageField(upload_to='pics/ButtonHole')

    def __str__(self):
        return self.button_hole_style


class Collar(models.Model):
    collar_style = models.CharField(max_length=50)
    collar_image = models.ImageField(upload_to='pics/Collar')

    def __str__(self):
        return self.collar_style


class Back(models.Model):
    back_style = models.CharField(max_length=50)
    back_image = models.ImageField(upload_to='pics/Back')

    def __str__(self):
        return self.back_style

class Pocket(models.Model):
    pocket_style = models.CharField(max_length=50)
    pocket_image = models.ImageField(upload_to='pics/Pocket')

    def __str__(self):
        return self.pocket_style

class Front(models.Model):
    front_style = models.CharField(max_length=50)
    front_image = models.ImageField(upload_to='pics/Front')

    def __str__(self):
        return self.front_style

class Color(models.Model):
    color_style = models.CharField(max_length=50)

    def __str__(self):
        return self.color_style

class Pattern(models.Model):
    pattern_style = models.CharField(max_length=50)

    def __str__(self):
        return self.pattern_style

class ClothType(models.Model):
    cloth_type_style = models.CharField(max_length=50)

    def __str__(self):
        return self.cloth_type_style

#-------------------------------------------------------------


class StandardSize(models.Model):
    standard_size_style = models.CharField(max_length=50)

    def __str__(self):
        return self.standard_size_style


class ClothMenu(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='pics/ClothMenu')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='Color')
    pattern = models.ForeignKey(Pattern, on_delete=models.CASCADE, related_name='pattern')
    cloth_type = models.ForeignKey(ClothType, on_delete=models.CASCADE, related_name='clothtype')
    collar = models.ForeignKey(Collar, on_delete=models.CASCADE, related_name='collar_cm')
    cuff = models.ForeignKey(Cuff, on_delete=models.CASCADE, related_name='cuff_cm')
    back = models.ForeignKey(Back, on_delete=models.CASCADE, related_name='back_cm')
    button = models.ForeignKey(Button, on_delete=models.CASCADE, related_name='button_cm')
    button_hole = models.ForeignKey(ButtonHole, on_delete=models.CASCADE, related_name='buttonhole_cm')
    pocket = models.ForeignKey(Pocket, on_delete=models.CASCADE, related_name='pocket_cm')
    front = models.ForeignKey(Front, on_delete=models.CASCADE, related_name='front_cm')
    price = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(1.0)])
    standard_size = models.ForeignKey(StandardSize, on_delete=models.CASCADE, related_name='standardsize_cm')

    def __str__(self):
        return self.name
#-------------------------------------------------------------
# model to connect these above models
#-------------------------------------------------------------

class OrderStatusCode(models.Model):
    status = models.CharField(max_length=25)
    def __str__(self):
        return self.status

class ShirtFit(models.Model):
    shirt_fit_style = models.CharField(max_length=50)

    def __str__(self):
        return self.shirt_fit_style

class Measurement(models.Model):
    profile_name = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userm', null=True, blank=True)
    shirt_fit = models.ForeignKey(ShirtFit, on_delete=models.CASCADE, related_name='shirtfit')
    neck = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1.0)])
    chest = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1.0)])
    waist = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1.0)])
    hips = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1.0)])
    shirt_length = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1.0)])
    shoulders = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1.0)])
    sleeve_length = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1.0)])
    cuff = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1.0)])
    arm_hole = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1.0)])
    biceps = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1.0)])
    height = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1.0)])
    weight = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(1.0)])
    def __str__(self):
        return self.profile_name

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    cloth_menu = models.ForeignKey(ClothMenu, on_delete=models.CASCADE, related_name='clothmenu', null=True, blank=True)
    collar = models.ForeignKey(Collar, on_delete=models.CASCADE, related_name='collar', null=True, blank=True)
    cuff = models.ForeignKey(Cuff, on_delete=models.CASCADE, related_name='cuff', null=True, blank=True)
    back = models.ForeignKey(Back, on_delete=models.CASCADE, related_name='back', null=True, blank=True)
    button = models.ForeignKey(Button, on_delete=models.CASCADE, related_name='button', null=True, blank=True)
    button_hole = models.ForeignKey(ButtonHole, on_delete=models.CASCADE, related_name='buttonhole', null=True, blank=True)
    pocket = models.ForeignKey(Pocket, on_delete=models.CASCADE, related_name='pocket', null=True, blank=True)
    front = models.ForeignKey(Front, on_delete=models.CASCADE, related_name='front', null=True, blank=True)
    size = models.ForeignKey(Measurement, on_delete=models.CASCADE, related_name='Measurement', null=True, blank=True)
    shirtfit = models.ForeignKey(ShirtFit, on_delete=models.CASCADE, related_name='shirtfitd', null=True, blank=True)
    standard_size = models.ForeignKey(StandardSize, on_delete=models.CASCADE, related_name='standardsize', null=True, blank=True)
    subtotal = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(1.0)])
    quantity = models.IntegerField(null=True, blank=True)
    status = models.ForeignKey(OrderStatusCode,  on_delete=models.CASCADE, related_name='orderstatuscode', null=True, blank=True)
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Orders'
        verbose_name_plural = 'Order_set'

