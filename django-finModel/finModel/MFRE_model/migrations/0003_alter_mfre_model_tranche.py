# Generated by Django 4.2.7 on 2023-12-26 07:05

import MFRE_model.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MFRE_model', '0002_mfre_model_delete_todo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mfre_model',
            name='tranche',
            field=MFRE_model.models.Tranche(blank=True, loanToValue=0.0, null=True),
        ),
    ]
