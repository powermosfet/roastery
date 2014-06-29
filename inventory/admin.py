import models
from django.contrib import admin

class VendorPayableInline(admin.TabularInline):
    model = models.VendorPayable
    readonly_fields = [
        'selflink'
    ]

class VendorReceivableInline(admin.TabularInline):
    model = models.VendorReceivable
    readonly_fields = [
        'selflink'
    ]

class VendorAdmin(admin.ModelAdmin):
    inlines = [
        VendorPayableInline,
        VendorReceivableInline,
        ]  
    list_display = [
        'name',
        'website',
        'vendorpayable',
        'vendorreceivable',
        ]

admin.site.register(models.CoffeeBag)
admin.site.register(models.Variety)
admin.site.register(models.Vendor, VendorAdmin)
admin.site.register(models.VendorPayable)
admin.site.register(models.VendorReceivable)
admin.site.register(models.InventoryAccount)

