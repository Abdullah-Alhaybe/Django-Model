# Generated by Django 3.2.8 on 2022-01-16 22:58

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('VZ', '0005_progress'),
    ]

    operations = [
        migrations.CreateModel(
            name='intern',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opschema', models.CharField(choices=[('ja', 'ja'), ('nee', 'nee')], default=[1], max_length=200)),
                ('opschema_toelichting', models.CharField(max_length=500)),
                ('hulp_nodig', models.CharField(choices=[('ja', 'ja'), ('nee', 'nee')], default=[1], max_length=200)),
                ('hulpsoort', multiselectfield.db.fields.MultiSelectField(choices=[('Ik heb meer informatie nodig', 'Ik heb meer informatie nodig'), ('meer ondersteuning nodig', 'meer ondersteuning nodig'), ('meer budget nodig', 'meer budget nodig'), ('meer uren nodig', 'meer uren nodig')], default=[1], max_length=87)),
                ('hulp_toelichting', models.CharField(max_length=500)),
                ('bespreek_punt', models.CharField(choices=[('ja', 'ja'), ('nee', 'nee')], default=[1], max_length=200)),
                ('onderwerp', models.CharField(max_length=500)),
                ('nieuwsbrief', models.CharField(choices=[('ja', 'ja'), ('nee', 'nee')], default=[1], max_length=200)),
                ('nieuwsbrief_toelichting', models.CharField(max_length=500)),
                ('external_gesprek', models.CharField(choices=[('ja', 'ja'), ('nee', 'nee')], default=[1], max_length=200)),
                ('met_wie', models.CharField(max_length=500)),
                ('wat_besproken', models.CharField(max_length=500)),
                ('resultaat', models.CharField(max_length=500)),
                ('link_relatie_profiel', models.CharField(choices=[('ja', 'ja'), ('nee', 'nee')], default=[1], max_length=200)),
                ('belangrijke_beslissing', models.CharField(choices=[('ja', 'ja'), ('nee', 'nee')], default=[1], max_length=200)),
                ('welke', models.CharField(max_length=500)),
                ('overleg_werkgroep', models.CharField(max_length=500)),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='VZ.project')),
            ],
        ),
    ]