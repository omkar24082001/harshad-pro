from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail 
from django.conf import settings


# Create your views here.
def contact(request):
    return render(request,"edu/contact.html") 


def submit_form(request): 
    if request.method == "POST":
        # Ensure you are getting the POST data from request.POST
        name = request.POST.get("name") 
        email = request.POST.get("email") 
        subject = request.POST.get("subject")  
        message = request.POST.get("message")   
        
        # Validate email format
        if "@" in email: 
            email_subject = f"New message from {name}: {subject}"
            email_message = f"Message: {message}\n\nFrom: {name}\nSender's Email : {email}"
            send_mail(
                email_subject,
                email_message,
                settings.EMAIL_HOST_USER,  
                ["harshadchavan92@gmail.com","rawoolomkar861@gmail.com" ],
               
                fail_silently=False,
                )
            messages.success(request, "The message has been sent successfully!") 
            return redirect('contact')  # Render on success
        else:
            messages.error(request, "Your email is invalid. Please enter a correct email address.") 
            return redirect('contact')  # Render on error
    messages.error(request,"This is not a POST method")
    return redirect('contact')  # Render the form for GET requests

    

