# Generated by Django 3.2.10 on 2022-01-03 17:41

from django.db import migrations

import trovi.fields


class Migration(migrations.Migration):

    dependencies = [
        ("trovi", "0004_alter_artifact_owner_urn"),
    ]

    operations = [
        migrations.AlterField(
            model_name="artifact",
            name="owner_urn",
            field=trovi.fields.URNField(max_length=254),
        ),
    ]
