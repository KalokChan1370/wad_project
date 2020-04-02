# Generated by Django 2.2.3 on 2020-04-02 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gamer_view', '0006_auto_20200402_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='madeby_name',
        ),
        migrations.AddField(
            model_name='reviews',
            name='madeby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
