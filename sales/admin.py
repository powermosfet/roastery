import models
from django.contrib import admin

class OrderInline(admin.TabularInline):
    model = models.Order

class CustomerAdmin(admin.ModelAdmin):
    inlines = [
        OrderInline,
    ]

admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Order)
