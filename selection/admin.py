import csv
from django.http import HttpResponse
from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Cuff, Collar, Orders, Measurement,ClothMenu, ShirtFit, Back, ClothType, Color, Front, Pattern, Pocket, StandardSize, Button, ButtonHole, OrderStatusCode
from customer.models import UserDetails
from payment.models import OrderHistory
admin.site.unregister(Group)
admin.site.site_header = 'Stitches Admin Page'
admin.site.site_title = 'Stitches Admin Page'
admin.site.site_url = '/admin_new/'
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

class ClothMenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'price', 'standard_size', 'color', 'pattern', 'cloth_type']

class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ['userref', 'address', 'phone', 'gender']

class OrderHistoryAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ['user', 'orderdate', 'price', 'deliverydate', 'orderlist']

    actions = ["export_as_csv"]

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['user', 'cloth_menu', 'size', 'standard_size', 'quantity', 'subtotal', 'status']
    list_editable = ['status']
    search_fields = ['user', 'cloth_menu']
    list_filter = ['user', 'cloth_menu', 'status']

# Register your models here.
admin.site.register(OrderHistory,OrderHistoryAdmin)
admin.site.register(Orders,OrdersAdmin)
admin.site.register(UserDetails,UserDetailsAdmin)
admin.site.register(ClothMenu, ClothMenuAdmin)
admin.site.register(StandardSize)
admin.site.register(OrderStatusCode)
admin.site.register(Cuff)
admin.site.register(Collar)
admin.site.register(ShirtFit)
admin.site.register(Pocket)
admin.site.register(Pattern)
admin.site.register(Front)
admin.site.register(Color)
admin.site.register(ClothType)
admin.site.register(Back)
admin.site.register(ButtonHole)
admin.site.register(Button)


