# Generated by Django 4.2.3 on 2023-07-15 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_student_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Учится'),
        ),
    ]
