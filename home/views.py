from django.shortcuts import render,redirect
from .models import Check_in,Review
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        people = request.POST.get('people')
        room_type = request.POST.get('room')
        check = Check_in(name=name,email=email,phone_number=phone,number_of_people=people,room_type=room_type)
        check.save()
        messages.success(request,"Your request has been accepted, we will call you in 24 hours")
        return redirect("/")
    allreviews = Review.objects.all()
    context = {'reviews':allreviews}
    return render(request,'index.html',context)