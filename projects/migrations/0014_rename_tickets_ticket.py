# Generated by Django 4.1.3 on 2022-11-05 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("projects", "0013_remove_tickets_category_tickets_product"),
    ]

    operations = [
        migrations.RenameModel(old_name="Tickets", new_name="Ticket",),
    ]
