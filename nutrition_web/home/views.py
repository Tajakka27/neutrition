from django.shortcuts import render
from home.models import *
from django.shortcuts import render, get_object_or_404
from .models import Testimonial
# Create your views here.
from django.shortcuts import render,HttpResponse
from django.urls import reverse
# Create your views here.



def service_detail(request, service_id):
    personal_info = SiteDescription.objects.first()
    service = get_object_or_404(Service, pk=service_id)
    return render(request, 'service_detail.html', {'personal_info': personal_info, 'service': service, 'active_page': 'services'})

def testimonial_detail(request, testimonial_id):
    personal_info = SiteDescription.objects.first()
    testimonial = get_object_or_404(Testimonial, pk=testimonial_id)
    return render(request, 'testimonial_detail.html', {'personal_info': personal_info, 'testimonial': testimonial, 'active_page': 'reviews'})

def home(request):
    personal_info = SiteDescription.objects.first()
    testimonials = Testimonial.objects.all()
    services = Service.objects.all()
    
    return render(request, 'home.html', {'personal_info': personal_info, 'testimonials': testimonials, 'services': services, 'active_page': 'home'})

def about_us_more(request):
    personal_info = SiteDescription.objects.first()  # Assuming there's only one instance
    return render(request, 'description.html', {'personal_info': personal_info, 'active_page': 'about'})
    # context ={ 'name':'tajakka', 'course': 'Django'}
    # return render(request,'index.html',context)



def appointment(request):
    personal_info = SiteDescription.objects.first()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        concerns = request.POST.get('concerns')
        pdf_document = request.FILES.get('pdf_document')

        if name and phone:
            ins = Appointment(name=name, email=email, phone=phone, concerns=concerns, pdf_document=pdf_document)
            ins.save()
            messages.success(request, 'Your appointment has been successfully scheduled!')
            # Redirecting to the same page after form submission
            return render(request, 'appointment.html', {'success_message': 'Your appointment has been successfully scheduled!'})
        else:
            messages.error(request, 'Name and phone number are required fields!')

    return render(request, 'appointment.html',{'personal_info': personal_info })


   
def payment_view(request):
    personal_info = SiteDescription.objects.first()  # Assuming there's only one instance
    return render(request, 'payment.html', {'personal_info': personal_info, 'active_page': 'payment'})