# Generated by Django 2.2.24 on 2021-08-05 14:24

import django.db.models.deletion
from django.db import migrations, models
from shuup_mirage_field.fields import EncryptedCharField


class Migration(migrations.Migration):

    dependencies = [
        ("shuup", "0095_reindex_catalog"),
    ]

    operations = [
        migrations.CreateModel(
            name="EncryptedConfigurationItem",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("key", models.CharField(max_length=100, verbose_name="key")),
                ("value", EncryptedCharField(max_length=255, verbose_name="value")),
                (
                    "shop",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="shuup.Shop",
                        verbose_name="shop",
                    ),
                ),
            ],
            options={
                "verbose_name": "configuration item",
                "verbose_name_plural": "configuration items",
                "unique_together": {("shop", "key")},
            },
        ),
    ]
