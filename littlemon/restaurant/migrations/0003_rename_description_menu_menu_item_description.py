# Generated by Django 4.2.8 on 2024-03-19 05:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0002_menu_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="menu", old_name="description", new_name="menu_item_description",
        ),
    ]
