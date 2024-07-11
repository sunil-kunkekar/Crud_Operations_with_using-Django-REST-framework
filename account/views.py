from django.shortcuts import render
from account.models import Employee
from account.serializers import EmployeeSerializer
from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class EmployeeView(viewsets.ModelViewSet):
    queryset         = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list (self,request, *args, **kwargs):
        queryset    = self.get_queryset()
        Serializers = self.get_serializer(queryset,many=True)

        return Response (Serializers.data)

    def create (self,request,*args,**kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        self.perform_create(serializers)

        headers = self.get_success_headers(serializers.data)
        return Response(serializers.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def retrieve (self,request,*args, **kwargs):
        queryset   = self.get_queryset()
        serializer = self.get_serializer(queryset,many=True)
        return Response(serializer.data)
    
    def update(self,request,*args,**kwargs):
        partial = kwargs.pop('partial',False)
        instance = self.get_object()
        serializer = self.get_serializer(instance,data=request.data,partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

