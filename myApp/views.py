from rest_framework import viewsets

from .models import Employee, ActivityPeriod
from .serializers import EmployeeSerializer, ActivityPeriodSerializer


# viewset for employee list includes their active time as well
class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# viewset for employee Active time list list
class ActivityPeriodView(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer
