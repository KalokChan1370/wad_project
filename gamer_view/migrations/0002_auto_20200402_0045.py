# Generated by Django 2.2.3 on 2020-04-01 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamer_view', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='category',
            new_name='cat',
        ),
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='page',
            name='gamename',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='time_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
