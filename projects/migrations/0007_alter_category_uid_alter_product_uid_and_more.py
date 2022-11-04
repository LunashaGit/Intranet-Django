# Generated by Django 4.1.2 on 2022-11-04 11:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_category_uid_alter_product_uid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('1cf7f45a-a8a2-44dc-a9df-678b24eb57fe'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('1cf7f45a-a8a2-44dc-a9df-678b24eb57fe'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('1cf7f45a-a8a2-44dc-a9df-678b24eb57fe'), editable=False, primary_key=True, serialize=False),
        ),
    ]
