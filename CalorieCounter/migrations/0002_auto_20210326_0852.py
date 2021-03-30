# Generated by Django 3.1.6 on 2021-03-26 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CalorieCounter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='quantity',
        ),
        migrations.AddField(
            model_name='food',
            name='servingSize',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='food',
            name='servingSizeUnits',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userfood',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AlterField(
            model_name='userfood',
            name='food',
            field=models.ManyToManyField(to='CalorieCounter.Food'),
        ),
        migrations.AlterField(
            model_name='userfood',
            name='user',
            field=models.ManyToManyField(blank=True, to='CalorieCounter.UserProfile'),
        ),
    ]