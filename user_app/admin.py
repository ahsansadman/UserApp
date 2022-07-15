from django.contrib import admin
from .models import Address, Parent, Child
# Register your models here.

class AddressInline(admin.TabularInline):
    model = Address

class ChildInline(admin.TabularInline):
    model = Child

class ParentAdmin(admin.ModelAdmin):
    inlines = [ChildInline]

admin.site.register(Address)
admin.site.register(Parent, ParentAdmin)
admin.site.register(Child)