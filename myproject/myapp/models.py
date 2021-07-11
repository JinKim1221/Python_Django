from django.db import models
from django.urls import reverse

# Create your models here.
# Model : use database without sql
# data is used as an object
# model = table
# field of model = column of table
# instance = record of table
# value of field = value in the table

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    # What fields decide
    # 1. Sort of colunm of database
    # 2. Restrictions (number of words)
    # 3. Sort of form
    # 4. Restrictions of form
    
    def __str__(self) :
        return "name : " + self.site_name + ", address : " + self.url

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
        
# Model made -> what type of data will be into database
# migration -> model is informed in database(create table)
# makemigrations -> record of change of model