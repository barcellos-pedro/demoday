# Generated by Django 2.2.1 on 2019-05-20 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horasBemApp', '0003_auto_20190520_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='Instituicao',
            field=models.CharField(choices=[('MACK', 'Universidade Presbiteriana Mackenzie'), ('PUCSP', 'Pontifícia Universidade Católica de São Paulo'), ('UMESP', 'Universidade Metodista de São Paulo'), ('UNAERP', 'Universidade de Ribeirão Preto'), ('UNIMEP', 'Universidade Metodista de Piracicaba'), ('UNISA', 'Universidade de Santo Amaro'), ('UNISANT ANNA', 'Universidade Sant Anna'), ('FEBASP', 'Centro Universitário Belas Artes de São Paulo'), ('FMU', 'Centro Universitário das Faculdades Metropolitanas Unidas'), ('SENAC', 'Centro Universitário Senac-São Paulo'), ('UNASP', 'Centro Universitário Adventista de São Paulo'), ('UNISAL', 'Centro Universitário Salesiano de São Paulo'), ('BSP', 'Business School São Paulo'), ('FGV', 'Fundação Getúlio Vargas'), ('ESPM', 'Escola Superior de Propaganda e Marketing'), ('FCL', 'Faculdade Cásper Líbero'), ('FAPCOM', 'Faculdade Paulus de Comunicação e Tecnologia')], max_length=15),
        ),
        migrations.DeleteModel(
            name='Instituicao',
        ),
    ]
