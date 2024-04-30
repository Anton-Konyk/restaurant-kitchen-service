# Generated by Django 5.0.4 on 2024-04-30 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dish",
            options={"verbose_name": "Dish", "verbose_name_plural": "Dishes"},
        ),
        migrations.AlterModelOptions(
            name="dishtype",
            options={
                "ordering": ["name"],
                "verbose_name": "Dish Type",
                "verbose_name_plural": "Dish Types",
            },
        ),
        migrations.AlterField(
            model_name="cook",
            name="prax_years",
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
