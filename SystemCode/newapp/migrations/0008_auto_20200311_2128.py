# Generated by Django 3.0.3 on 2020-03-11 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0007_auto_20200305_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='socialservice',
            name='medishield_opt_out',
        ),
        migrations.AddField(
            model_name='socialservice',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='socialservice',
            name='annual_value',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='socialservice',
            name='ethnic_group',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='socialservice',
            name='medishield',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='socialservice',
            name='pioneer_merdeka',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]