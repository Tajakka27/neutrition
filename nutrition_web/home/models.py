from django.db import models
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save


from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30, null=True)
    phone = models.CharField(max_length=30)
    cause = models.TextField(max_length=450, null=True)
    pdf_document = models.FileField(upload_to='pdf_documents/', null=True, blank=True)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"


class SiteDescription(models.Model):
    # motto = models.CharField(max_length=100)
    # short_description = models.CharField(max_length=200)
    long_description = models.TextField()
    full_description_First_Pera = models.TextField(null=True)
    full_description_Second_Pera = models.TextField(null=True)
    full_description_Third_Pera = models.TextField(null=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    availabe_times = models.TextField(null=True)
    location = models.TextField(null=True)
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    about_us_image = models.ImageField(upload_to='about_us_images', null=True, blank=True)
    First_banner_image = models.ImageField(upload_to='banner_images', null=True, blank=True)
    Second_banner_image = models.ImageField(upload_to='banner_images', null=True, blank=True)
    Third_banner_image = models.ImageField(upload_to='banner_images', null=True, blank=True)

    #additional fields for payment
    bkash_phone_No = models.CharField(max_length=20, null=True, blank=True)
    bkash_transaction_id = models.CharField(max_length=50, null=True, blank=True)
    nagad_phone_No = models.CharField(max_length=20, null=True, blank=True)
    nagad_transaction_id = models.CharField(max_length=50, null=True, blank=True)
    rocket_phone_No = models.CharField(max_length=20, null=True, blank=True)
    rocket_transaction_id = models.CharField(max_length=50, null=True, blank=True)

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValidationError as e:
            messages.warning(request, str(e))

    def __str__(self):
        return f"Email: Email: {self.email}, Phone: {self.phone}"
    
 
    

@receiver(pre_save, sender=SiteDescription)
def limit_personal_information(sender, instance, **kwargs):
    # Check if there is already an instance of PersonalInformation
    if SiteDescription.objects.exists() and not instance.pk:
        existing_instance = SiteDescription.objects.first()
        # Log the action
        LogEntry.objects.log_action(
            user_id=1,  # Set the user ID of the admin who made the change
            content_type_id=ContentType.objects.get_for_model(SiteDescription).pk,
            object_id=existing_instance.pk,
            object_repr=str(existing_instance),
            action_flag=ADDITION,
            change_message='Replaced existing PersonalInformation instance'
        )
        # Delete the existing instance
        existing_instance.delete()



class Testimonial(models.Model):
    Client_Name = models.CharField(max_length=30, null=True)
    Profession = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to='testimonial_images')
    review = models.TextField()

    def __str__(self):
        return self.review


# class AvailableTime(models.Model):
#     DAYS_CHOICES = (
#         ('Monday', 'Monday'),
#         ('Tuesday', 'Tuesday'),
#         ('Wednesday', 'Wednesday'),
#         ('Thursday', 'Thursday'),
#         ('Friday', 'Friday'),
#         ('Saturday', 'Saturday'),
#         ('Sunday', 'Sunday'),
#     )

#     day = models.CharField(max_length=20, choices=DAYS_CHOICES)
#     start_time = models.TimeField()
#     end_time = models.TimeField()

#     def __str__(self):
#         return f"{self.day} {self.start_time.strftime('%I:%M %p')} - {self.end_time.strftime('%I:%M %p')}"
    

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    logo = models.ImageField(upload_to='service_logos/', null=True, blank=True)

    def __str__(self):
        return self.name
    
