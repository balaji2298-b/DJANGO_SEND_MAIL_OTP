from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
import random

def index(request):
    return render(request, "index.html")

# Generate a 4-digit OTP
def generateOTP():
    return ''.join(random.choices("0123456789", k=4))

# Send OTP to email
def send_otp(request):
    if request.method == "POST":
        email = request.POST.get("email")
        otp = generateOTP()
        request.session['otp'] = otp  # Store in session
        request.session['email'] = email  # Optional: store email too

        # Send email
        html_content = f"<p>Your OTP is <strong>{otp}</strong></p>"
        send_mail(
            "Your OTP Code",
            otp,
            "your_email@example.com",
            [email],
            fail_silently=False,
            html_message=html_content
        )
        return HttpResponse("OTP sent")
    return HttpResponse("Invalid request")

# Verify OTP
def verify_otp(request):
    if request.method == "POST":
        entered_otp = request.POST.get("otp")
        session_otp = request.session.get("otp")

        if entered_otp == session_otp:
            return HttpResponse("OTP Verified")
        else:
            return HttpResponse("Invalid OTP")
    return HttpResponse("Invalid request")
