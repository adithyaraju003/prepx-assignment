# Generated by Django 4.1.1 on 2023-07-29 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exp', '0002_alter_expense_created_at_alter_expense_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
