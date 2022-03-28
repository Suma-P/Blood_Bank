from django.db import models


# Create your models here.


class District(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Branch(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class BloodGroup(models.Model):
    name = models.CharField(max_length=250)

    # choices = ({'A +ve': 'A +ve'}, {'A -ve': 'A -ve'}, {'B +ve': 'B +ve'}, {'B -ve': 'B -ve'}, {'AB +ve': 'AB +ve'},
    #            {'AB -ve': 'AB -ve'}, {'O +ve': 'O +ve'}, {'O -ve': 'O -ve'})

    def __str__(self):
        return self.name


class Donor(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    gender = models.CharField(max_length=40)
    mobile = models.IntegerField()
    address = models.CharField(max_length=250)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.SET_NULL, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name
