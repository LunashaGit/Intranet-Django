# Generated by Django 4.1.2 on 2022-11-04 08:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_category_slug_product_slug_alter_category_uid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('80cbeee0-b5d8-42b7-97a4-40d2bdbdff4b'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('80cbeee0-b5d8-42b7-97a4-40d2bdbdff4b'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('80cbeee0-b5d8-42b7-97a4-40d2bdbdff4b'), editable=False, primary_key=True, serialize=False),
        ),
    ]
