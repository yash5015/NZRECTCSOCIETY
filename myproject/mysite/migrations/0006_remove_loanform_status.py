# Generated by Django 3.2.7 on 2022-02-09 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0005_auto_20220209_1317'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loanform',
            name='status',
        ),
    ]