# Generated by Django 5.1.6 on 2025-03-04 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='images/default', upload_to='images/'),
        ),
    ]
