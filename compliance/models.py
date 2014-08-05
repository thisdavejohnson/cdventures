from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

class Employee(models.Model):
    employer = models.ForeignKey(Organization)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    birthday = models.DateTimeField()
    avgHoursWorked = models.IntegerField(default=0)
    addressFirstLine = models.CharField(max_length=200)
    addressSecondLine = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    race = models.CharField(max_length=200)

    # (exempt / non-exempt)
    flsaStatus = models.CharField(max_length=200)

    veteranStatus = models.CharField(max_length=200)
    
    # active duty military status
    milStatus = models.CharField(max_length=200)

