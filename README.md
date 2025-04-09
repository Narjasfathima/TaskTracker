Task-Management-System
Setup Instructions

-> Create a directory, open cmd in directory path and clone TaskTracker project

        git clone https://github.com/Narjasfathima/TaskTracker.git
-> Install Virtual environment

        pip install virtualenv
-> Create virtual environment within the directory.

        python -m venv venv_name  # On Windows
        python3 -m venv venv_name  # On macOS/Linux
-> Activate virtual environmant

        venv_name\Scripts\activate       # On Windows           
        source venv_name/bin/activate     # On macOS/Linux
-> Open VendorNexus in VScode

       code .
-> Open terminal in vscode, navigate to project directory

       cd tasktracker
-> Install requirements.txt

     pip install -r requirements.txt

-> Create migration file and apply on database
  
      py manage.py makemigrations
      py manage.py migrate

-> Create a superuser (That is superadmin)
     
      python manage.py createsuperuser
 
-> Run the server and follow link
    
      py manage.py runserver
      
-> The project uses swagger UI, that allows developers to visualize and interact with the APIs (Application Programming Interfaces).

-> Follow the link. In a web application login can perform only either super admin or admin
  After login, super admin can perform all features. But admin can perform only task related features.


-> swagger UI documentation added for API
    
    endpoint: /swagger/user/

-> JWT authentication, Authorize using following

    Bearer 'accesstoken'

API Endpoints:-

1)Login -   Return accecctoken and refresh token

    Endpoint: /User/login/
    
    Method:
        Post: View List of task
        
     Data:JSON 
          {"username": "string", "password": "string"}
          
    Permission: User, Admin, Super admin

2)Task view  -   Fetch all tasks assigned to the logged-in user

      Endpoint: /User/tasks/
      
      Method:
          Get: View List of task

      Permission: User

3)  Method: PUT (Update task status)
    
        Endpoint: /User/tasks/{id}:
        
        Data:JSON 
          {"status": "string", "completion_report": "string", "worked_hours": "int"}
        
        Permission: User

      
4)  Method: GET (List report of particular completed task)

        Endpoint: /User/tasks/{id}/report/    
    
        Permission: Admin and Super admin
