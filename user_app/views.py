from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics, status
from .serializers import AddressSerializer, ParentSerializer, ChildSerializer
from .models import Address, Parent, Child
from django.http import Http404
# Create your views here.

class ParentView(generics.ListAPIView):
    """
    List all parents or create a new parent
    """
    
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    def get(self, request):
        try:
            parent = self.get_queryset()
            serializer = self.get_serializer(parent, many=True)
            return Response(serializer.data)
        except Parent.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
class ChildrenView(generics.ListAPIView):   
    """
    List all children or create a new children
    """
       
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    
    def get(self, request):
        try:
            children = self.get_queryset()
            serializer = self.get_serializer(children, many=True)
            return Response(serializer.data)
        except Child.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ParentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a parent instance.
    """
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    lookup_field = "id"
    
    def get(self,request,id):
        try:
            data = self.get_object()
            serializer = self.get_serializer(data)
            return Response(serializer.data)
        except Parent.DoesNotExist:
            raise Http404        

    def put(self, request, id):
        data = self.get_object()
        serializer = self.get_serializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            data = self.get_object()
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT) 
        except Parent.DoesNotExist:
            raise Http404       
        
class ChildDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a child instance.
    """
    queryset = Child.objects.all()
    serializer_class = ChildSerializer
    lookup_field = "id"
    
    def get(self,request, id):
        try:
            data = self.get_object()
            serializer = self.get_serializer(data)
            return Response(serializer.data)
        except Child.DoesNotExist:
            raise Http404        

    def put(self, request, id, format=None):
        data = self.get_object()
        serializer = self.get_serializer(data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        try:
            data = self.get_object()
            data.delete()
            return Response(status=status.HTTP_204_NO_CONTENT) 
        except Child.DoesNotExist:
            raise Http404       
        