# Generated by Django 3.2.25 on 2024-08-27 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('monitoramento', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParametrosTratamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parametro', models.CharField(max_length=100)),
                ('valor_minimo', models.DecimalField(decimal_places=2, max_digits=4)),
                ('valor_maximo', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='RecomendacaoTratamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recomendacoes', models.TextField()),
                ('medicao', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='recomendacao', to='monitoramento.medicao')),
            ],
        ),
    ]
