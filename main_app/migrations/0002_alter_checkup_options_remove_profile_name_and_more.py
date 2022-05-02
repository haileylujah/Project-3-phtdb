# Generated by Django 4.0.4 on 2022-05-02 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='checkup',
            options={'ordering': ['-date']},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(default='123 somewhere road, someplace', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='1234567890', max_length=15),
            preserve_default=False,
        ),
    ]
