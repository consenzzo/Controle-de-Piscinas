# Generated by Django 3.2.25 on 2024-08-27 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField(auto_now_add=True)),
                ('ph', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cloro', models.DecimalField(decimal_places=2, max_digits=4)),
                ('alcalinidade', models.DecimalField(decimal_places=2, max_digits=4)),
                ('piscina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicoes', to='core.piscina')),
            ],
        ),
    ]
