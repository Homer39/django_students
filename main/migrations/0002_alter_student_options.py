# Generated by Django 4.2.3 on 2023-07-15 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('last_name',), 'verbose_name': 'Студент', 'verbose_name_plural': 'Студенты'},
        ),
    ]
