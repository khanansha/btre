from django.db import models

# Create your models here.
from django.db import models
from datetime import datetime

"""
  LISTING
id = INT
realtor = INT (FOREIGN KEY [realtor])
title = STR
address = STR
city = STR
state = STR
zipcode = STR
description = TEXT
price = INT
bedrooms = INT
bathrooms = INT
garage = INT [0]
sqft = INT
lot_size = FLOAT
is_published = BOOL [true]
list_date = DATE
photo_main = STR
photo_1 = STR
photo_2 = STR
photo_3 = STR
photo_4 = STR
photo_5 = STR
photo_6 = STR


### REALTOR
id = INT
name = STR
photo = STR
description = TEXT
email = STR
phone = STR
is_mvp = BOOL [0]
hire_date = DATE


### CONTACT
id = INT
user_id = INT
listing = INT
listing_id = INT
name = STR
email = STR
phone = STR
message = TEXT
contact_date = DATE



"""

class Realtor(models.Model):
    name = models.CharField(max_length=300)
    photo =  models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
   