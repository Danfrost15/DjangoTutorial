# Generated by Django 5.0.1 on 2024-02-04 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_students_regno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students_regno',
            name='reg_no',
            field=models.CharField(max_length=11),
        ),
    ]
