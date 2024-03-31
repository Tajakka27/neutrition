from django.contrib import admin
from django.urls import path,include
from home import views
from django.conf import settings
from django.conf.urls.static import static


#admin header customization 

admin.site.site_header = "Log in to Admin Panel"
admin.site.site_title = "Welcome to the admin site"
admin.site.index_title = "welcome to this portal"

urlpatterns = [
    path('', views.home, name='home'),   
    path('appointment', views.appointment, name='appointment'),
    path('about_us_more', views.about_us_more, name='about_us_more'),
    path('payment/', views.payment_view, name='payment'),
    path('testimonial/<int:testimonial_id>/', views.testimonial_detail, name='testimonial_detail') ,
    path('services/<int:service_id>/', views.service_detail, name='service_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)