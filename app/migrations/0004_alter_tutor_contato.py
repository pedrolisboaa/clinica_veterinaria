# Generated by Django 3.2.22 on 2023-12-13 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_tutor_contato'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutor',
            name='contato',
            field=models.CharField(max_length=11),
        ),
    ]
