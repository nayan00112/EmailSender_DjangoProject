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