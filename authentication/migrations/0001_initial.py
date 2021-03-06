# Generated by Django 3.2.12 on 2022-03-12 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('conf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Nombre de usuario')),
                ('email', models.CharField(max_length=254, unique=True, verbose_name='Correo electrónico')),
                ('nombres', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombres')),
                ('apellidos', models.CharField(blank=True, max_length=200, null=True, verbose_name='Apellidos')),
                ('identificacion', models.CharField(max_length=10, unique=True, verbose_name='Identificación')),
                ('direccion', models.CharField(max_length=500, verbose_name='Direccion domiciliaria')),
                ('telefono', models.CharField(max_length=50, verbose_name='Teléfono')),
                ('usuario_activo', models.BooleanField(default=True)),
                ('usuario_administrador', models.BooleanField(default=False)),
                ('imagen', models.ImageField(max_length=200, null=True, upload_to='user/', verbose_name='Imagen de perfil')),
                ('roles', models.ManyToManyField(db_column='rol_usuario', to='conf.Rol')),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
    ]
