# Generated by Django 3.0.7 on 2020-08-11 10:37

from django.db import migrations, models
import django.db.models.deletion
import sport.models.medical_group_reference


class Migration(migrations.Migration):

    dependencies = [
        ('sport', '0034_auto_20200810_0645'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalGroupReference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=sport.models.medical_group_reference.get_reference_path)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sport.Student')),
            ],
            options={
                'db_table': 'medical_group_reference',
            },
        ),
    ]
