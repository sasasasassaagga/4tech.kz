# Generated by Django 5.1.6 on 2025-03-03 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='accounts/images/'),
        ),
    ]
