# Generated by Django 4.2 on 2023-04-07 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                ("idx", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=50, null=True)),
                ("tel", models.CharField(blank=True, max_length=50, null=True)),
                ("email", models.CharField(blank=True, max_length=50, null=True)),
                ("address", models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]