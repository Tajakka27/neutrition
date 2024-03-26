from django.db import models
from django.dispatch import receiver
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.admin.models import LogEntry, ADDITION
from django.contrib.contenttypes.models import ContentType
from django.db.models.signals import pre_save


class Appointment(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=30)
    time = models.ForeignKey('AvailableTime', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name +' ' + self.phone



class PersonalInformation(models.Model):
    motto = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    long_description = models.TextField()
    full_description_First_Pera = models.TextField(null=True)
    full_description_Second_Pera = models.TextField(null=True)
    full_description_Third_Pera = models.TextField(null=True)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    location = models.TextField(null=True)
    profile_image = models.ImageField(upload_to='profile_images', null=True, blank=True)
    about_us_image = models.ImageField(upload_to='about_us_images', null=True, blank=True)

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValidationError as e:
            messages.warning(request, str(e))

    def __str__(self):
        return f"Motto: {self.motto}, Email: {self.email}, Phone: {self.phone}"
    
 
    

@receiver(pre_save, sender=PersonalInformation)
def limit_personal_information(sender, instance, **kwargs):
    # Check if there is already an instance of PersonalInformation
    if PersonalInformation.objects.exists() and not instance.pk:
        existing_instance = PersonalInformation.objects.first()
        # Log the action
        LogEntry.objects.log_action(
            user_id=1,  # Set the user ID of the admin who made the change
            content_type_id=ContentType.objects.get_for_model(PersonalInformation).pk,
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


class AvailableTime(models.Model):
    DAYS_CHOICES = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    )

    day = models.CharField(max_length=20, choices=DAYS_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.day} {self.start_time.strftime('%I:%M %p')} - {self.end_time.strftime('%I:%M %p')}"