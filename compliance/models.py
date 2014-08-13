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
    addressSecondLine = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    race = models.CharField(max_length=200, blank=True)

    # (exempt / non-exempt)
    flsaStatus = models.CharField(max_length=200, blank=True)

    veteranStatus = models.CharField(max_length=200, blank=True)
    
    # active duty military status
    milStatus = models.CharField(max_length=200, blank=True)

# this class represents the result of a user answering the set of survey questions
class Survey(models.Model)
    numEmployees = models.IntegerField(default=0)
    
    NONPROFIT = 'NP'
    PUBLIC = 'PB'
    PRIVATE = 'PR'
    UNION = 'UN'
    EMPLOYMENTAGENCY = 'EA'
    STATEGOVERNMENT = 'SG'
    LOCALGOVERNMENT = 'LG'
    FEDERALCONTRACTOR = 'FC'
    FEDERALSUBCONTRACTOR = 'FS'

    ORG_TYPE_CHOICES = (
        (NONPROFIT, 'Non-profit'),
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
        (STATEGOVERNMENT, 'State Government'),
        (LOCALGOVERNMENT, 'Local Government'),
        (FEDERALCONTRACTOR, 'Federal Contractor'),
        (FEDERALSUBCONTRACTOR, 'Federal Sub-contractor'),
    )

    orgType = models.CharField(max_length=2,
                               choices=ORG_TYPE_CHOICES,
                               default=private)

    # contracts amount over $25k?
    contractsSize = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name