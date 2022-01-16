# Generated by Django 3.2.8 on 2022-01-16 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('doel', models.CharField(max_length=500)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('budget', models.IntegerField()),
                ('bestuurder_1', models.CharField(max_length=200)),
                ('bestuurder_2', models.CharField(max_length=200)),
                ('kerngroep', models.CharField(max_length=200)),
                ('werkgroep', models.CharField(max_length=200)),
                ('werkgroepleden', models.CharField(max_length=200)),
                ('projectfase', models.CharField(choices=[('Ontwerpfase', 'Ontwerpfase'), ('Realisatiefase', 'Realisatiefase')], max_length=200)),
            ],
        ),
    ]