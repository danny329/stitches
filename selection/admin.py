from django.contrib import admin
from .models import Cuff, Collar, Design, Measurement, ShirtFit, Back, ClothType, Color, Front, Pattern, Pocket, StandardSize, Button, ButtonHole

# Register your models here.

admin.site.register(Cuff)
admin.site.register(Collar)
admin.site.register(Design)
admin.site.register(Measurement)
admin.site.register(StandardSize)
admin.site.register(ShirtFit)
admin.site.register(Pocket)
admin.site.register(Pattern)
admin.site.register(Front)
admin.site.register(Color)
admin.site.register(ClothType)
admin.site.register(Back)
admin.site.register(ButtonHole)
admin.site.register(Button)
