# Generated by Django 5.1.4 on 2024-12-09 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("wikiApp", "0002_tema"),
    ]

    operations = [
        migrations.AlterField(
            model_name="articulo",
            name="descripcionArticulo",
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]