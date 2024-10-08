# Generated by Django 5.0.8 on 2024-08-07 19:19

import django.db.models.deletion
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='criado')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='ativo')),
                ('cargo', models.CharField(max_length=100, verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='criado')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='ativo')),
                ('servico', models.CharField(max_length=100, verbose_name='servico')),
                ('descricao', models.CharField(max_length=200, verbose_name='descricao')),
                ('icone', models.CharField(choices=[('lni-cog', 'engrenagem'), ('lni-starts-up', 'grafico'), ('lni-users', 'usuarios'), ('lni-layers', 'design'), ('lni-mobile', 'mobile'), ('lni-rocket', 'foguete')], max_length=20, verbose_name='icone')),
            ],
            options={
                'verbose_name': 'Servico',
                'verbose_name_plural': 'Serviços',
            },
        ),
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='criado')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='modificado')),
                ('ativo', models.BooleanField(default=True, verbose_name='ativo')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('bio', models.TextField(max_length=255, verbose_name='Bio')),
                ('imagem', stdimage.models.StdImageField(force_min_size=False, upload_to='equipe', variations={'thumb': {'crop': True, 'height': 480, 'width': 480}}, verbose_name='Imagem')),
                ('facebook', models.CharField(default='#', max_length=100, verbose_name='Facebook')),
                ('twitter', models.CharField(default='#', max_length=100, verbose_name='Twitter')),
                ('instagram', models.CharField(default='#', max_length=100, verbose_name='Instagram')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cargo', verbose_name='Cargo')),
            ],
            options={
                'verbose_name': 'Funcionario',
                'verbose_name_plural': 'Funcionarios',
            },
        ),
    ]
