
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('v1/parent/<int:id>', ParentDetailView.as_view(), name='parent_detail'),
    path('v1/child/<int:id>', ChildDetailView.as_view(), name='child_detail'),
    path('v1/parent/', ParentView.as_view(), name='parent'),
    path('v1/children/', ChildrenView.as_view(), name='children'),
]
