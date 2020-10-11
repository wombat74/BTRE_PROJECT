from django.db import models
from datetime import datetime
from realtors.models import Realtor

# When model creation is complete we will move the model to the database.
# Step 1. pip install pillow (this is needed for the ImageFields, must be done before makemigrations)
# Step 2. python manage.py makemigrations (this will create a file that we will run to migrate the model)
# Optional: to see actual SQL before migrating: python manage.py sqlmigrate listings 0001
# Step 3. python manage.py migrate (this does the actual migration to the db)

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    desctiption = models.TextField(blank=True) # blank=True: so that will not error if blank. OOPS MISSPELLED IT!!
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/') # link to mediafolder
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # link to mediafolder
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # link to mediafolder
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # link to mediafolder
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # link to mediafolder
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # link to mediafolder
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) # link to mediafolder
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
