# Generated by Django 2.2.3 on 2019-07-31 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_remove_profile_full_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('board', '0007_remove_slide_advertising_slide_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main_Advertising',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('AD_profile', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_Advertising', to='users.Profile')),
                ('name', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, related_name='main_Advertising', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
