from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.

class project(models.Model):
    project_fase = (
        ('Ontwerpfase','Ontwerpfase'),
        ('Realisatiefase','Realisatiefase')
         )

    programs = (
        ('Deltaplan','Deltaplan'),
        ('Thuis in het Zeeuwse Verpleeghuis','Thuis in het Zeeuwse Verpleeghuis'),
        ('Uitvoeringsagenda','Uitvoeringsagenda'),
        ('Zeeuwse Zorg Coalitie','Zeeuwse Zorg Coalitie'),
        ('Communicatie/evenementen','Communicatie/evenementen')
    )


    project_name = models.CharField(max_length=200)
    program = models.CharField(max_length=200,choices=programs,default=[1])
    doel = models.CharField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    budget = models.IntegerField()
    bestuurder_1 = models.CharField(max_length=200)
    bestuurder_2 = models.CharField(max_length=200)
    kerngroep = models.CharField(max_length=200)
    werkgroep = models.CharField(max_length=200)
    werkgroepleden = models.CharField(max_length=200)
    projectfase = models.CharField(max_length=200,choices=project_fase)


