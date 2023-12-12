# Generated by Django 4.2.6 on 2023-10-27 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'categorias',
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'distritos',
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name_plural': 'provincias',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('apellido', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('contraseña', models.CharField(max_length=250)),
                ('n_celular', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'usuarios',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=250)),
                ('descripcion', models.CharField(max_length=250)),
                ('peso', models.DecimalField(decimal_places=2, max_digits=4)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=4)),
                ('ancho', models.DecimalField(decimal_places=2, max_digits=4)),
                ('largo', models.DecimalField(decimal_places=2, max_digits=4)),
                ('material', models.CharField(max_length=250)),
                ('color', models.CharField(max_length=250)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=4)),
                ('image', models.ImageField(upload_to='venta/images')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.categoria')),
            ],
            options={
                'verbose_name_plural': 'productos',
            },
        ),
    ]