# Generated by Django 2.2.3 on 2020-04-02 14:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamer_view', '0008_auto_20200402_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='REVIEW_ID',
        ),
    ]
