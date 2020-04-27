# Generated by Django 2.2.10 on 2020-04-16 18:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_package'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='package',
            name='Package',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='package',
            name='price',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='package',
            name='proview',
            field=models.CharField(default='', max_length=100),
        ),
    ]
