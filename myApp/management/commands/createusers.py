import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from myApp.models import Employee, ActivityPeriod


class Command(BaseCommand):
    help = 'Create 4 users'

    def handle(self, *args, **options):
        # to increase the number of dummy employees, increase the range for i

        for i in range(4):
            name = random.choice(('Chris', 'Dwayne', 'Bradley', 'Tom', 'Peter', 'Tony'))
            last_name = random.choice(('Martyn', 'England', 'Parker', 'Dsouza'))
            user_id = random.randint(2000000, 9000000)
            time_zone = random.choice(('Asia/Kolkata', 'America/Los_Angeles', 'Asia/Tokyo', 'Australia/Sydney'))

            # create employees
            employee = Employee.objects.create(name=f'{name} {last_name}', user_id=f'W{user_id}', timezone=time_zone)

            for j in range(3):
                day = random.randint(30, 120)
                minutes = random.randint(1, 60)
                start_time = datetime.now()
                random_active_time = random.randint(15, 60) #to increase time-difference between start and end time

                # create active periods
                active_period = ActivityPeriod.objects.create(employee=employee,
                                                              start_time=(start_time + timedelta(days=day,minutes=minutes)).strftime('%Y-%m-%d %H:%M'),
                                                              end_time=(start_time + timedelta(days=day,minutes=minutes + random_active_time)).strftime('%Y-%m-%d %H:%M'))
        return "Users created succesfully"
