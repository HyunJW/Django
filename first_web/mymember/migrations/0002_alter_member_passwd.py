# Generated by Django 4.2 on 2023-04-17 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mymember", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="member",
            name="passwd",
            field=models.CharField(max_length=500),
        ),
    ]
