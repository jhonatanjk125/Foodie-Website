# Generated by Django 4.2.6 on 2023-10-25 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userprofile_longuitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover_photo',
            field=models.ImageField(blank=True, null=True, upload_to='users/cover_photos'),
        ),
    ]