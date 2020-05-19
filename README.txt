# django-rest-framework-api
 Simple API with Django and the Django Rest Framework

 Run the following commands to get started:

 $ virtualenv env
 $ pip install -r requirement.txt
 $ python manage.py runserver





To create dummydata run custom management command:

 $ python manage.py createusers


createusers.py file location:

 myApp/
    __init__.py
    models.py
    management/
        commands/
            __init__.py
            createusers.py
    tests.py
    views.py
    
    
    
 after creating dummy data run the server:
 
  $ python manage.py runserver
  
  
 Now go to 'localhost:8000/myApp/' and click on value of "employee" key 
 
