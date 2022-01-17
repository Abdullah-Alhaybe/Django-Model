# Generated by Django 3.2.8 on 2022-01-17 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VZ', '0006_intern'),
    ]

    operations = [
        migrations.AddField(
            model_name='intern',
            name='kosten_budget',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='intern',
            name='uren_budget',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='exact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uren_bestede', models.IntegerField(default=0)),
                ('kosten_bestede', models.IntegerField(default=0)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='VZ.project')),
            ],
        ),
    ]
