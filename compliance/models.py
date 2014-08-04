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
    employeeID = models.IntegerField(default=0)
