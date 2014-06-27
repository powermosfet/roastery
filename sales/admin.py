import models
import roast.models as roast
from django.contrib import admin

def create_modeladmin(modeladmin, model, name = None):
    class  Meta:
        proxy = True
        app_label = model._meta.app_label

    attrs = {'__module__': '', 'Meta': Meta}

    newmodel = type(name, (model,), attrs)

    admin.site.register(newmodel, modeladmin)
    return modeladmin

class OrderInline(admin.TabularInline):
    model = models.Order
    readonly_fields = [
        'selflink'
    ]

class CustomerAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline,
    ]

admin.site.register(models.Customer, CustomerAdmin)

class BatchInline(admin.TabularInline):
    model = roast.Batch
    readonly_fields = [
        'selflink'
    ]

class OrderAdmin(admin.ModelAdmin):
    inlines = [
        BatchInline,
    ]
    list_display = [
        '__unicode__',
        'variety',
        'quantity',
        'customer',
        'date',
        'done',
    ]

admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.CustomerPayable)
admin.site.register(models.CustomerReceivable)

