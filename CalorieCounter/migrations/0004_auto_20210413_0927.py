# Generated by Django 3.1.6 on 2021-04-13 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CalorieCounter', '0003_auto_20210413_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfood',
            name='food',
        ),
        migrations.AddField(
            model_name='userfood',
            name='food',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='CalorieCounter.food'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='userfood',
            name='user',
        ),
        migrations.AddField(
            model_name='userfood',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
