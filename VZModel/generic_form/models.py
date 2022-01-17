from django.db import models

# Create your models here.

class klanten(models.Model):
    klant = models.CharField(max_length=200)
    E_mail = models.EmailField(max_length=250)


class Questionnaire(models.Model):
    Questionnaire_kind = (
        ('New project','New project'),
        ('Progress','Progress'),
        ('Internal','Internal')
    )

    klant = models.ForeignKey(klanten,null=True,on_delete=models.SET_NULL)
    questionnaire_kind = models.CharField(max_length=200,choices=Questionnaire_kind,default=[1])

class Question(models.Model):
    CATEGORY = (
    ('Multichoice', 'Multichoice'),
    ('Choose N', 'Choose N'),
    ('Text', 'Text'),
    ('Number','Number')
)

    questionnaire = models.ManyToManyField(Questionnaire)
    question_text = models.CharField(max_length=200,verbose_name="Questionnaire name",null=True,default=None,blank=True)
    question_category = models.CharField(max_length=200,verbose_name="Question category",null=False,choices=CATEGORY,default=None,blank=False)


class Answer(models.Model):
    question = models.ForeignKey(Question,null=True,on_delete=models.SET_NULL)
    answer = models.CharField(max_length=200)
