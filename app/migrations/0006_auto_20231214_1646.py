# Generated by Django 3.2.22 on 2023-12-14 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20231214_1557'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='pet',
        ),
        migrations.AddField(
            model_name='pet',
            name='tutor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.tutor'),
        ),
    ]
