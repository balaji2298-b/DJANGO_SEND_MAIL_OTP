from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
import math, random

# Create your views here.
def index(request):
    return render(request,"index.html")


def generateOTP() :
    digits = "0123456789"
    OTP = ""
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
    return OTP

def send_otp(request):
    email=request.POST.get("email")
    o=generateOTP()
    htmlgen = '<p>Your OTP is <strong>'+o+'</strong></p>'
    send_mail('OTP request',o,'jobsearcher@gmail.com',[email],fail_silently=False,html_message=htmlgen)
    return HttpResponse(o)



   