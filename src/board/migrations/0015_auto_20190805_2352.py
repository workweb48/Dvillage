# Generated by Django 2.2.3 on 2019-08-05 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0014_auto_20190805_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='board',
            name='board_image',
            field=models.ImageField(default=False, upload_to='images'),
        ),
    ]