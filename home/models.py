from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
people_choice= (
                ("1", "1"),
                ("2", "2"),
                ("3", "3"),
                ("4", "4"),
                ("5", "5"),
                ("6", "6"),
                ("7", "7"),
                ("8", "8"),
                ("9", "9"),
                )

room_choices = (
    ("Deluxe","Deluxe"),
    ("family","family"),
    ("Somiking","Somiking")
)

ratings_choices = (
    ("1 Star","1 Star"),
    ("2 Star","2 Star"),
    ("3 Star","3 Star"),
    ("4 Star","4 Star"),
    ("5 Star","5 Star")
)
# Create your models here.
class Check_in(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    number_of_people = models.CharField(choices=people_choice,max_length=10,null=False)
    room_type = models.CharField(max_length=100,choices=room_choices,null=False,default="Deluxe")
    def __str__(self):
        return self.name


class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.CharField(choices=ratings_choices,default="5 Star",max_length=100)
    review = models.TextField()
    image = models.ImageField(upload_to="images",default="")
    timestamp = models.DateField(default=now)
    def __str__(self):
        return "Review by " +self.name
    