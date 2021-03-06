# Generated by Django 2.2.3 on 2019-10-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0022_topic_advertising_ad_topics'),
    ]

    operations = [
        migrations.CreateModel(
            name='Up_img',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('up_img_upload', models.ImageField(default=True, upload_to='images')),
                ('url_img', models.URLField(max_length=250)),
                ('active_img', models.BooleanField(default=False)),
            ],
        ),
    ]
