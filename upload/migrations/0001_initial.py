# Generated by Django 4.0.2 on 2022-05-26 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('college', models.CharField(blank=True, max_length=50, null=True)),
                ('degree', models.CharField(blank=True, max_length=50, null=True)),
                ('skills', models.TextField(blank=True, max_length=50, null=True)),
                ('designation', models.CharField(blank=True, max_length=50, null=True)),
                ('company', models.CharField(blank=True, max_length=50, null=True)),
                ('file_location', models.CharField(blank=True, max_length=50, null=True)),
                ('text_file_location', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
