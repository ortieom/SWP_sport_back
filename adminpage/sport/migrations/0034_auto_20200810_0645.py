# Generated by Django 3.0.7 on 2020-08-10 03:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0033_auto_20200703_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='minimum_medical_group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='sport.MedicalGroup'),
        ),
    ]
