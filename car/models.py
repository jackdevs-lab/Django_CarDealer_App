from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from django.conf import settings

class Car(models.Model):
    fuel_type_choices = (
        ('lpg', 'LPG'),
        ('cng', 'CNG'),
        ('petrol', 'Petrol'),
        ('diesel', 'Diesel'),
        ('electric', 'Electric'),
    )
    car_owner_choices = (
        ('first owner', 'First Owner'),
        ('second owner', 'Second Owner'),
        ('third owner', 'Third Owner'),
        ('fourth owner or more', 'Fourth Owner or More'),
    )
    insurance_type_choices = (
        ('comprehensive', 'Comprehensive'),
        ('third party', 'Third Party'),
        ('expired', 'Expired'),
    )
    registration_type_choices = (
        ('individual', 'Individual'),
        ('corporate', 'Corporate'),
        ('taxi', 'Taxi'),
    )
    car_status_options = (
        ('active','Active'),
        ('deactive','Deactive'),
    )
    vehicle_type_choices = (
        ('Car','Car'),
        ('Bike','Bike'),
        ('Truck','Truck'),
        ('Tractor','Tractor'),
        ('Auto Rickshaw','Auto Rickshaw'),
        ('Agriculture Instrument','Agriculture Instrument'),
    )
    transmission_type_choices = (
		('automatic', 'Automatic'),
		('manual', 'Manual'),
	)

    city_choices = (
		('Nairobi', 'Nairobi'),
('Mombasa', 'Mombasa'),
('Kisumu', 'Kisumu'),
('Nakuru', 'Nakuru'),
('Eldoret', 'Eldoret'),
('Thika', 'Thika'),
('Nyeri', 'Nyeri'),
('Naivasha', 'Naivasha'),
('Machakos', 'Machakos'),
('Meru', 'Meru'),
('Embu', 'Embu'),
('Kericho', 'Kericho'),
('Kakamega', 'Kakamega'),
('Malindi', 'Malindi'),
('Garissa', 'Garissa'),
('Kitale', 'Kitale'),
('Nanyuki', 'Nanyuki'),
('Bungoma', 'Bungoma'),
('Isiolo', 'Isiolo'),
('Voi', 'Voi'),
('Narok', 'Narok'),
('Kilifi', 'Kilifi'),
('Lamu', 'Lamu'),
('Busia', 'Busia'),
('Murang’a', 'Murang’a'),
('Kiambu', 'Kiambu'),
('Taveta', 'Taveta'),
('Homa Bay', 'Homa Bay'),
('Siaya', 'Siaya'),
('Migori', 'Migori'),
('Mandera', 'Mandera'),
('Wajir', 'Wajir'),
('Marsabit', 'Marsabit'),
('Baringo', 'Baringo'),
('Lodwar', 'Lodwar'),
('Kapenguria', 'Kapenguria'),
('Chuka', 'Chuka'),
('Maua', 'Maua'),
('Oyugis', 'Oyugis'),
('Kajiado', 'Kajiado'),
('Sotik', 'Sotik'),
('Ol Kalou', 'Ol Kalou'),
('Nyahururu', 'Nyahururu'),
('Wundanyi', 'Wundanyi'),
('Kwale', 'Kwale'),
('Tana River', 'Tana River'),
('Bomet', 'Bomet'),
('Maralal', 'Maralal'),
('Moyale', 'Moyale'),
('Other', 'Other'),

		
	)
        
        

    car_id = models.AutoField
    car_title = models.CharField( max_length=100)
    make_year = models.IntegerField()
    make_month = models.CharField( max_length=100, blank=True, null = True )
    car_manufacturer = models.CharField( max_length=100)
    car_model = models.CharField( max_length=100)
    car_version = models.CharField( max_length=100, blank=True, null = True )
    car_color = models.CharField( max_length=100, blank=True, null = True )
    fuel_type = models.CharField(max_length=25, choices=fuel_type_choices, default= 'petrol')
    transmission_type = models.CharField(max_length=25, choices=transmission_type_choices, default= 'manual')
    car_owner = models.CharField(max_length=25, choices=car_owner_choices, default= 'first owner')
    kilometer_driven = models.IntegerField(blank=True, null = True )
    expected_selling_price = models.IntegerField()
    registration_type = models.CharField(max_length=25, choices=registration_type_choices, default= 'individual')
    insurance_type = models.CharField(max_length=25, choices=insurance_type_choices, default= 'expired')
    registration_number = models.CharField( max_length=30, blank=True, null = True )
    car_description = models.TextField(blank=True, null = True )
    car_post_date = models.DateField(default=datetime.now)
    car_photo = models.ImageField(upload_to='car/car_images/', blank=True, null=True)    # car_other_photos = models.ImageField(upload_to='cars')
    car_status = models.CharField(max_length=25, choices=car_status_options, default= 'active')
    vehicle_type = models.CharField(max_length=25, choices=vehicle_type_choices, default= 'Car')


    # user , Many to One connection
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # settings.AUTH_USER_MODEL
    # personal details

    car_owner_phone_number = models.IntegerField(default=0, blank=True, null = True )
    car_city = models.CharField( max_length=50, choices=city_choices, default= 'Patna')
    car_owner_name = models.CharField( max_length=100,default="-")


    class Meta:
        # order of cars in admin area
        # use -publish instead of publish , to reverse the order
        ordering = ('car_title',)

    def __str__(self):
        # responsible to show name of carin admin instead of object1
        # also look the authoradmin class in admin.py 
        return self.car_title


# To set privacy policies from the admin area.
class Privacy(models.Model):
    privacy_policy = models.TextField()

    def __str__(self):
        # responsible to show name of carin admin instead of object1
        # also look the authoradmin class in admin.py 
        return self.privacy_policy
    class Meta:
        verbose_name_plural = "Privacy"

#To display some advertisement images
class Ads(models.Model):

    popup_ad = models.ImageField(upload_to='car/car_images/', blank=True, null=True)
    popup_ad_url = models.URLField(max_length=400, blank=True, null = True )
    ad1 = models.ImageField(upload_to='car/car_images/', blank=True, null=True)
    ad1_url = models.URLField(max_length=400, blank=True, null = True )
    ad2 = models.ImageField(upload_to='car/car_images/', blank=True, null=True)
    ad2_url = models.URLField(max_length=400, blank=True, null = True )


    def __str__(self):
        # responsible to show name of carin admin instead of object1
        # also look the authoradmin class in admin.py 
        return str(self.popup_ad)
    
    class Meta:
        verbose_name_plural = "Ads"

#clients, are the users that try to access car information
#They are not required to login and register with email and password
#They are required to submit phone number for otp verification
class Client(models.Model):
    name = models.CharField( max_length=100,default="-",blank=True, null = True)
    phone_number = models.IntegerField(default=0)


    def __str__(self):
        # responsible to show name of car in admin instead of object1
        # also look the authoradmin class in admin.py 
        return str(self.name)
    
    class Meta:
        verbose_name_plural = "Client Phone Number"
def __str__(self):
        return self.car_title


class CarPhoto(models.Model):
    car = models.ForeignKey(Car, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car/car_images/')

    def __str__(self):
        return f"Photo for {self.car.car_title}"
