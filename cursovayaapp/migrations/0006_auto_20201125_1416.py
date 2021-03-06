# Generated by Django 3.1.3 on 2020-11-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cursovayaapp', '0005_auto_20201125_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='username',
            new_name='login',
        ),
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='employee',
            name='privilegies',
            field=models.BooleanField(default=0),
        ),
    ]
