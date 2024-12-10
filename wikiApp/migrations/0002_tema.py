# Generated by Django 5.1.4 on 2024-12-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wikiApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="tema",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombreTema", models.CharField(blank=True, max_length=128, null=True)),
                (
                    "descripcionTema",
                    models.CharField(blank=True, max_length=512, null=True),
                ),
            ],
        ),
    ]