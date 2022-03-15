# Generated by Django 3.2.10 on 2022-01-11 20:37

import django.db.models.expressions
from django.db import migrations, models

import trovi.fields


class Migration(migrations.Migration):

    dependencies = [
        ("trovi", "0005_remove_default_owner_urn"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artifactversion",
            name="contents_urn",
            field=trovi.fields.URNField(max_length=254, null=True),
        ),
        migrations.AddIndex(
            model_name="artifact",
            index=models.Index(
                django.db.models.expressions.F("created_at"),
                name="artifact__created_at",
            ),
        ),
    ]
