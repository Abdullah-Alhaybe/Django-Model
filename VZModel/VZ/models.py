from email.policy import default
from pyexpat import model
from random import choices
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

    themas = (
        ('Kennis en Inzicht','Kennis en Inzicht'),
        ('Kiezen en Toeleiden','Kiezen en Toeleiden'),
        ('Leren en Opleiden','Leren en Opleiden'),
        ('Werken en Behoud','Werken en Behoud')
    )

    projectleiders = (
        ('Sophie Aberson','Sophie Aberson'),
        ('Rianne Deij','Rianne Deij'),
        ('Tamar Duivewaarde','Tamar Duivewaarde'),
        ('Anjali Geensen','Anjali Geensen')
    )

    partners = (
        ('ADRZ','ADRZ'),
        ('CZ Zorgkantoor','CZ Zorgkantoor'),
        ('Emergis','Emergis'),
        ('Hoornbeek','Hoornbeek')
    )


    project_name = models.CharField(max_length=200)
    program = models.CharField(max_length=200,choices=programs,default=[1])
    thema =  MultiSelectField(choices=themas,default=[1])
    project_leider= MultiSelectField(choices=projectleiders,default=[1])
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
    partner = MultiSelectField(choices=partners,default=[1])


    def __str__(self):
        return self.project_name

class progress(models.Model):
    periods = (
        ('januari t/m maart 2022','januari t/m maart 2022'),
        ('april t/m Juni 2022','april t/m Juni 2022'),
        ('juli t/m september 2022','juli t/m september 2022'),
        ('oktober t/m december 2022','oktober t/m december 2022')
    )

    project_fase = (
        ('Ontwerpfase','Ontwerpfase'),
        ('Realisatiefase','Realisatiefase')
         )

    leermoments = (
        ('ja','ja'),
        ('nee','nee')
    )


    project = models.ForeignKey(project,null=True,on_delete=models.SET_NULL)
    period = models.CharField(max_length=200,choices=periods,default=[1])
    projectfase = models.CharField(max_length=200,choices=project_fase,default=[1])
    uitgevoerde_activiteit = models.CharField(max_length=500)
    behaalde_doel = models.CharField(max_length=500)
    verwachte_activiteit = models.CharField(max_length=500)
    verwachte_doel = models.CharField(max_length=500)
    leermoment = models.CharField(max_length=200,choices=leermoments,default=[1])
    leermoment_toelichting =models.CharField(max_length=500)


    # def __str__(self):
    #     return self.project



class intern(models.Model):
    ja_nee = (
        ('ja','ja'),
        ('nee','nee')
    )

    hulp_soort = (
        ('Ik heb meer informatie nodig','Ik heb meer informatie nodig'),
        ('meer ondersteuning nodig','meer ondersteuning nodig'),
        ('meer budget nodig','meer budget nodig'),
        ('meer uren nodig','meer uren nodig')
    )

    project = models.ForeignKey(project,null=True,on_delete=models.SET_NULL)
    opschema = models.CharField(max_length=200,choices=ja_nee,default=[1])
    opschema_toelichting = models.CharField(max_length=500)
    hulp_nodig = models.CharField(max_length=200,choices=ja_nee,default=[1])
    hulpsoort = MultiSelectField(choices=hulp_soort,default=[1])
    hulp_toelichting = models.CharField(max_length=500)
    bespreek_punt= models.CharField(max_length=200,choices=ja_nee,default=[1])
    onderwerp = models.CharField(max_length=500)
    nieuwsbrief = models.CharField(max_length=200,choices=ja_nee,default=[1])
    nieuwsbrief_toelichting = models.CharField(max_length=500)
    external_gesprek = models.CharField(max_length=200,choices=ja_nee,default=[1])
    met_wie = models.CharField(max_length=500)
    wat_besproken = models.CharField(max_length=500)
    resultaat = models.CharField(max_length=500)
    link_relatie_profiel = models.CharField(max_length=200,choices=ja_nee,default=[1])
    belangrijke_beslissing = models.CharField(max_length=200,choices=ja_nee,default=[1])
    welke = models.CharField(max_length=500)
    overleg_werkgroep = models.CharField(max_length=500)
    uren_budget =  models.IntegerField(default=0)
    kosten_budget =  models.IntegerField(default=0)


    # def __str__(self):
    #     return self.project


class exact(models.Model):
    project = models.ForeignKey(project,null=True,on_delete=models.SET_NULL)
    uren_bestede =  models.IntegerField(default=0)
    kosten_bestede =  models.IntegerField(default=0)