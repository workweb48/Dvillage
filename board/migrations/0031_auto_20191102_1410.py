# Generated by Django 2.2.3 on 2019-11-02 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0030_auto_20191102_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(blank=True, default=0, max_length=250),
            preserve_default=False,
        ),
    ]