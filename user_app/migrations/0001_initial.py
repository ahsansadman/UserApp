# Generated by Django 4.0.6 on 2022-07-14 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=50, verbose_name='Street')),
                ('city', models.CharField(max_length=50, verbose_name='City')),
                ('state', models.CharField(max_length=50, verbose_name='state')),
                ('zip', models.IntegerField(verbose_name='Zip')),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_app.address', verbose_name='Address')),
            ],
            options={
                'verbose_name': 'Parent',
                'verbose_name_plural': 'Parents',
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last Name')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child', to='user_app.parent', verbose_name='')),
            ],
            options={
                'verbose_name': 'Child',
                'verbose_name_plural': 'Children',
            },
        ),
    ]