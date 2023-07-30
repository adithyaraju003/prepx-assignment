# Generated by Django 4.1.1 on 2023-07-29 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='created_by',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='expense',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]