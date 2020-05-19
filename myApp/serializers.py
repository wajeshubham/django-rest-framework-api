from rest_framework import serializers

from .models import Employee, ActivityPeriod


class ActivityPeriodSerializer(serializers.ModelSerializer):
    # change the date format
    start_time = serializers.DateTimeField(format="%B %d %Y, %I:%M%p")
    end_time = serializers.DateTimeField(format="%B %d %Y, %I:%M%p")

    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')


class EmployeeSerializer(serializers.ModelSerializer):
    activity_period = ActivityPeriodSerializer(many=True)

    class Meta:
        model = Employee
        fields = ('user_id', 'name', 'timezone', 'activity_period',)
