# Generated by Django 2.2.1 on 2019-05-20 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horasBemApp', '0004_auto_20190520_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='foto',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]