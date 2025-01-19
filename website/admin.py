from django.contrib import admin
from .models import Record, Customer, Product, Order, Employee, Supplier

class RecordAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'city', 'created_at')
    list_filter = ('city', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    list_filter = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email')
    date_hierarchy = 'created_at'
    readonly_fields = ('email',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('price',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product', 'quantity', 'order_date', 'status')
    list_filter = ('status', 'order_date')
    search_fields = ('customer__first_name', 'customer__last_name', 'product__name')
    date_hierarchy = 'order_date'
    raw_id_fields = ('customer', 'product')

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'position', 'hired_date')
    list_filter = ('position',)
    search_fields = ('first_name', 'last_name')
    date_hierarchy = 'hired_date'
    readonly_fields = ('hired_date',)

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_name', 'phone')
    list_filter = ('name',)
    search_fields = ('name', 'contact_name')
    readonly_fields = ('name',)

admin.site.register(Record, RecordAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Supplier, SupplierAdmin)



# Register your models here.
