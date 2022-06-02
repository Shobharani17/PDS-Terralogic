# Generated by Django 4.0.2 on 2022-05-30 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0003_alter_employees_college_alter_employees_company_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='college',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='company',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='degree',
            field=models.CharField(blank=True, max_length=252, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='designation',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='file_location',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='name',
            field=models.CharField(blank=True, max_length=600, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='phone',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employees',
            name='text_file_location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]