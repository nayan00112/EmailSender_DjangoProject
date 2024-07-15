
# Django project [send email]

### We are going to make django app which can send email.

- make virtual environemtn



```bash
pip install virtualenv 
virtualenv myenv
cd myenv
cd Script
activate 
cd ../..
```

- install django

```
pip install django
```

- make django project
```
django-admin startproject EmailSender
cd EmailSender
```

- make app
``` 
python manage.py startapp home
```

- open setting.py file in Project folder and add app

```

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'home', # app name
]
```

- In your project's settings file (settings.py), add the following configurations for the email backend. For example, if you are using Gmail:

```
# settings.py

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_email_password'

```
Make sure to replace your_email@gmail.com and your_email_password with your actual email and password. You might want to use environment variables or a more secure method to handle these credentials in a production environment.

For Gmail, you should use an App Password instead of your regular Gmail account password. An App Password is a 16-digit passcode that allows less secure apps or devices to access your Google account. Here are the steps to generate an App Password:

### Steps to Generate an App Password for Gmail
- Enable 2-Step Verification:

- Go to your Google Account.
- Click on the Security tab.
- Under the Signing in to Google section, enable - 2-Step Verification if it's not already enabled.

### Generate App Password:
- After enabling 2-Step Verification, go back to the Security tab.
- Under the Signing in to Google section, you will see App passwords.
- Click on App passwords.
- You might need to enter your Google account password again.
- In the Select app dropdown, choose Mail.
- In the Select device dropdown, choose the device you’re using (or choose Other and give it a custom name).
- Click Generate.
- You will see a 16-digit password. Copy this password.

### views.py file of home app:

```
from django.shortcuts import render

from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def home(request):
    if request.method == "POST":
        email = request.POST['email']
        sub = request.POST['sub']
        tarea = request.POST['textarea']

        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(sub, tarea, email_from, recipient_list)

    return render(request, "index.html")
```

### configure urls.py in (home) app folder:

```
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
]
```

### urls.py in project folder
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('home.urls')),
]
```

### index.html
- Make 'templates' folder in (home) app.
- Make index.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form method="post">
        {% csrf_token %}
        Email: <input type="email" name="email">
        <br>
        Subject: <input type="text" name="sub">
        <br>
        Text <textarea name="textarea"></textarea>
        <br>
        <input type="submit" value="submit">
    </form>
</body>
</html>
```
- Tip: Enhance Your Loops with CSS

### Run server

```
python manage.py runserver
```

- Now test it.

---
By Nayan