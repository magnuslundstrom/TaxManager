# Generated by Django 3.1.6 on 2021-02-16 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movement',
            name='receiver',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='movement',
            name='sender',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='movement',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]