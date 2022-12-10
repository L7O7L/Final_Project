# Generated by Django 4.1.4 on 2022-12-10 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=200, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=200, verbose_name='Apellidos')),
                ('dni', models.CharField(max_length=8, unique=True, verbose_name='DNI')),
                ('email', models.EmailField(max_length=200, unique=True, verbose_name='Email')),
                ('telefono', models.CharField(max_length=9, unique=True, verbose_name='Telefono')),
            ],
            options={
                'verbose_name': 'Director',
                'verbose_name_plural': 'Directores',
            },
        ),
        migrations.CreateModel(
            name='Institucion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200, verbose_name='Nombre del colegio')),
                ('cod_modular', models.CharField(max_length=7, unique=True, verbose_name='Código Modular')),
                ('cod_local', models.CharField(max_length=6, unique=True, verbose_name='Código Local')),
                ('director', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='apirest.director')),
            ],
            options={
                'verbose_name': 'Institucion',
                'verbose_name_plural': 'Instituciones',
            },
        ),
        migrations.CreateModel(
            name='Tipo_user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Tipo de usuario',
                'verbose_name_plural': 'Tipos de usuarios',
            },
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=200, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=200, verbose_name='Apellidos')),
                ('fecha_nac', models.DateField(verbose_name='Fecha de nacimiento')),
                ('dni', models.CharField(max_length=8, unique=True, verbose_name='DNI')),
                ('email', models.CharField(max_length=200, unique=True, verbose_name='Correo electronico')),
                ('password', models.CharField(max_length=200, verbose_name='Contraseña')),
                ('telefono', models.CharField(max_length=9, verbose_name='Telefono')),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirest.institucion')),
            ],
            options={
                'verbose_name': 'Tutor',
                'verbose_name_plural': 'Tutores',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombres', models.CharField(max_length=200, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=200, verbose_name='Apellidos')),
                ('fecha_nac', models.DateField(verbose_name='Fecha de nacimiento')),
                ('dni', models.CharField(max_length=8, unique=True, verbose_name='DNI')),
                ('correo', models.EmailField(max_length=200, unique=True, verbose_name='Correo electronico')),
                ('password', models.CharField(max_length=200, verbose_name='Contraseña')),
                ('telefono', models.CharField(max_length=9, unique=True, verbose_name='Telefono')),
                ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirest.institucion')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirest.tipo_user')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apirest.tutor')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]
