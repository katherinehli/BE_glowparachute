# Generated by Django 4.2.7 on 2023-11-29 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MFRE_model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MFRE_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
    ]
