# Generated by Django 3.2.25 on 2024-07-02 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compfest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.CharField(editable=False, max_length=50, unique=True),
        ),
    ]
