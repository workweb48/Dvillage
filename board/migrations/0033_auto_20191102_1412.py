# Generated by Django 2.2.3 on 2019-11-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0032_auto_20191102_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]