# Generated by Django 4.0.6 on 2022-07-15 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0007_remove_address_user_parent_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='address',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_app.address'),
            preserve_default=False,
        ),
    ]
