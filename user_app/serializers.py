from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import Address, Parent, Child

class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Address
        fields = '__all__'
        
class ChildSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Child
        fields = '__all__'
        
class ParentSerializer(WritableNestedModelSerializer):
    children = ChildSerializer(many=True,read_only=True)
    address = AddressSerializer()
    class Meta:
        model = Parent
        fields = ['id', 'first_name', 'last_name', 'address', 'children']