from django.db import models
from django.utils import timezone


class Employee(models.Model):
    name = models.CharField(max_length=50)
    user_id = models.CharField(max_length=9)
    timezone = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    # to access queryset as property in serializers
    @property
    def activity_period(self):
        return self.activityperiod_set.all().order_by('start_time')


class ActivityPeriod(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_time = models.DateTimeField(default=timezone.now())
    end_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.employee.name + "'s active period"
