# Generated by Django 4.1.4 on 2022-12-10 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apirest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institucion',
            name='director',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='institucion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='institucion',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='tipo',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='tutor',
        ),
        migrations.DeleteModel(
            name='Director',
        ),
        migrations.DeleteModel(
            name='Institucion',
        ),
        migrations.DeleteModel(
            name='Tipo_user',
        ),
        migrations.DeleteModel(
            name='Tutor',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
