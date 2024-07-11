from django.urls import path,include 
from account.views import EmployeeView
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register(r'employees',EmployeeView)

urlpatterns = [
    path('',include(routers.urls)),
]