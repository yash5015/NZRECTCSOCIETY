# Generated by Django 4.0.1 on 2022-02-11 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0006_remove_loanform_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanform',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]