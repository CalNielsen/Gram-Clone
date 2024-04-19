[![Gram Clone 1.0 Logo](https://github.com/CalNielsen/Gram-Clone/blob/main/static/images/gram_clone_logo.png)](https://github.com/CalNielsen/Gram-Clone/)

![Version](https://img.shields.io/badge/Version-1.0-blue)

# Gram Clone 1.0
The Gram Clone repository contains the source code for the
**Gram Clone** web site (currently hosted locally).  


The Gram Clone web site was created as a project to learn django and allow family members to share, comment, and like photos or images.


# Project ScreenShots
## Home Page
![HomePage](https://github.com/CalNielsen/Gram-Clone/blob/main/static/images/screen_home.png)
<br/>
## Login Page
![LoginPage](https://github.com/CalNielsen/Gram-Clone/blob/main/static/images/screen_login.png)
<br/>
## Post Page
![PostPage](https://github.com/CalNielsen/Gram-Clone/blob/main/static/images/screen_post.png)
<br/>
## Profile Page
![ProfilePage](https://github.com/CalNielsen/Gram-Clone/blob/main/static/images/screen_profile.png)
<br/>
## See Other Pages through a browser

# Features
The **Gram Clone** web site models the Instagram application allowing users to login, upload photos and pictures, provide descriptions, comment on, and like other user uploaded images.

# Developer Notes
## Installation
  1. Clone Repository
  ```
  git clone https://github.com/CalNielsen/Gram-Clone/
  ```
  2. Choose/Install IDE
  *  Visual Studio
  3. Set up virtual environment
   ```
    % cd /Users/<user>/projects
    % mkdir Gram-Clone
    % cd Gram-Clone
    % python3 -m venv Venv
    % source Venv/bin/activate
  ```
  4. Install dependencies (under virtual environment)
  ```
    % [OPTIONAL] python3 -m pip install --upgrade pip (if "A new release of pip is available" is reported)
    % pip install django
    % pip install pillow
  ```

  ## Checking Versions
  ```
    % pip freeze (to see underlying django, asgircf, sqlparse vesions)
    % echo $0 (to see display the command shell environment)
    % which python3 (to diplay the location of python3)
    % python3 --version
    % python3 manage.py --version
    % python3 -m pip freeze
    % pip show django

  ```
  ## Starting/Configuring Project
  ```
    % sudo django-admin startproject ema .
    % cd /Users/<user>/projects/Gram-Clone/Venv (or a project directory where manage.py is located)
    % python3 manage.py makemigrations
    % python3 manage.py migrate
    % python3 manage.py createsuperuser
      username:admin  (for superuser access of 127.0.0.1:8000/admin (admin panel) pages)
      email address:  (legitimate email for project administrator)
      password:       (password for superuser account)
  ```

  ## Restarting the server
  You may need to restart the server (i.e. runserver), distributed with django, to 
  see model and other configured changes through the terminal window or
  Visual Studio.
  ```  
    % cntrl-c (in the terminal window running the server)
    % python3 manage.py runserver
  ``` 
  ## Launch a browser
  Enter the following URL to view Gram-Clone home page:
  ```
    http://127.0.0.1:8000/
  ``` 

  ## Allowing wifi connected devices to access the Django web server
  Identify the IP address of the connected device.  The ifconfig command or
  wifi device discovery tool (e.g. fing) may be used to identify the IP address
  of the device.  Note the IP address of the 'en0' physical network interface,
  using the ifconfig command, for devices that offer the command. 
  ```
    % ifconfig en0
  ```
  e.g. 192.168.86.35 

  Modify the settings.py to allow connections from specific wifi connected ip 
  addresses or wildcard all '*'
  ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.86.36', '192.168.86.24', '192.168.86.35','192.168.86.28']
  Start server on 0.0.0.0:8000
  ```
    % python3 -u manage.py runserver 0.0.0.0:8000
  ```
## Visual Studio
* Enter control+backquote (to open terminal window)


## Testing
As more automated tests are written, fewer manual tests will need to be done. Different
methods of running the automated tests are shown below:  
  ```
    % python3 manage.py test
    % python manage.py test --verbosity=2 (0-minimal,1-normal,2-verbose,3-very verbose)
    % python3 manage.py test Pages (to run tests below the Pages directory)
    % python3 manage.py test Pages.tests (to run tests in the Pages.tests module)
    % python3 -m unittest discover  > outt 2>&1
  ```
## Problem Tracking
Under consideration: 
* Jira
* GitHub Issues
* BugZilla 

# Resources
  * https://www.youtube.com/watch?v=41ek3VNx_6Q (Django Test Driven Development Cookbook)
  * https://docs.djangoproject.com/en/5.0/ref/django-admin/#inspectdb (Django inspectdb section)

