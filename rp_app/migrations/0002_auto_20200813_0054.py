# Generated by Django 3.1 on 2020-08-13 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rp_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clienturl',
            old_name='company',
            new_name='client',
        ),
        migrations.AlterField(
            model_name='clienturl',
            name='is_open_for_cache',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='companyclient',
            name='is_active',
            field=models.BooleanField(default=True, null=True),
        ),
    ]