# Generated by Django 2.2.3 on 2019-07-30 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190703_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.CharField(default=0, max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
