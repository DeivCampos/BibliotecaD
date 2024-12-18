# Generated by Django 4.2.16 on 2024-12-07 19:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('biografia', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('isbn', models.CharField(max_length=13)),
                ('cantidad_disponible', models.IntegerField()),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.autor')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.categoria')),
            ],
        ),
    ]
