# Generated by Django 2.2.10 on 2020-04-16 18:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200416_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='user',
        ),
    ]