# Generated by Django 4.0.4 on 2022-05-16 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mustafa', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['number'], 'verbose_name_plural': 'Öğrenciler'},
        ),
    ]