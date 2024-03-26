from django.shortcuts import render
from home.models import *

# Create your views here.
from django.shortcuts import render,HttpResponse
from django.urls import reverse
# Create your views here.


def home(request):
    personal_info = PersonalInformation.objects.first()  # Assuming there's only one instance
    testimonials = Testimonial.objects.all()
    return render(request, 'home.html', {'personal_info': personal_info, 'testimonials': testimonials})
    # context ={ 'name':'tajakka', 'course': 'Django'}
    # return render(request,'index.html',context)

def about_us_more(request):
    personal_info = PersonalInformation.objects.first()  # Assuming there's only one instance
    return render(request, 'description.html', {'personal_info': personal_info})
    # context ={ 'name':'tajakka', 'course': 'Django'}
    # return render(request,'index.html',context)



def appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        time_id = request.POST.get('time')  # Assuming time_id is sent from the form
        time = AvailableTime.objects.get(id=time_id)
        ins = Appointment(name=name, email=email, phone=phone, time=time)
        ins.save()
        print('The data has been saved to the database')
    available_times = AvailableTime.objects.all()
    return render(request, 'appointment.html', {'available_times': available_times})

   

# Create your views here.
