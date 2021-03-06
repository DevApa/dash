# Generated by Django 3.2.12 on 2022-03-12 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_column='nombre', max_length=300, unique=True)),
                ('address', models.TextField(db_column='direccion', max_length=1000, null=True)),
                ('phone', models.TextField(db_column='telefono', max_length=30, null=True)),
                ('director', models.TextField(db_column='director', max_length=300, null=True)),
                ('foundation_date', models.DateField(db_column='fecha_fundacion')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')),
                ('date_update', models.DateTimeField(auto_now=True, db_column='fecha_edicion')),
                ('date_input', models.TextField(db_column='hora_ingreso', max_length=5, null=True)),
                ('state', models.BooleanField(db_column='estado', default=True)),
            ],
            options={
                'db_table': 'org_unidad_Academica',
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_column='nombre', max_length=300, unique=True)),
                ('address', models.TextField(blank=True, db_column='direccion', max_length=1000, null=True)),
                ('phone', models.TextField(blank=True, db_column='telefono', max_length=30, null=True)),
                ('rector', models.TextField(db_column='rector', max_length=300, null=True)),
                ('type', models.TextField(choices=[('E', 'Estatal'), ('P', 'Privada')], db_column='tipo', max_length=1000, null=True)),
                ('foundation_date', models.DateField(db_column='fecha_fundacion')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')),
                ('date_update', models.DateTimeField(auto_now=True, db_column='fecha_edicion')),
                ('date_input', models.TextField(db_column='hora_ingreso', max_length=5, null=True)),
                ('state', models.BooleanField(db_column='estado', default=True)),
            ],
            options={
                'db_table': 'org_universidad',
            },
        ),
        migrations.CreateModel(
            name='SchoolOf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(db_column='nombre', max_length=300, unique=True)),
                ('address', models.TextField(db_column='direccion', max_length=1000, null=True)),
                ('phone', models.TextField(db_column='telefono', max_length=30, null=True)),
                ('dean', models.TextField(db_column='decano', max_length=300, null=True)),
                ('foundation_date', models.DateField(db_column='fecha_fundacion')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')),
                ('date_update', models.DateTimeField(auto_now=True, db_column='fecha_edicion')),
                ('date_input', models.TextField(db_column='hora_ingreso', max_length=5, null=True)),
                ('state', models.BooleanField(db_column='estado', default=True)),
                ('university', models.ForeignKey(db_column='univeridad', on_delete=django.db.models.deletion.CASCADE, to='organization.university')),
            ],
            options={
                'db_table': 'org_facultad',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='nombre', max_length=50)),
                ('phone', models.TextField(db_column='telefono', max_length=30, null=True)),
                ('foundation_date', models.DateField(db_column='fecha_fundacion')),
                ('date_created', models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')),
                ('date_update', models.DateTimeField(auto_now=True, db_column='fecha_edicion')),
                ('date_input', models.TextField(db_column='hora_ingreso', max_length=5, null=True)),
                ('state', models.BooleanField(db_column='estado', default=True)),
                ('academic_unit', models.ForeignKey(db_column='unidad_academica', on_delete=django.db.models.deletion.CASCADE, to='organization.academicunit')),
                ('boss', models.ForeignKey(db_column='jefe', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'name',
                'db_table': 'org_departamento',
            },
        ),
        migrations.AddField(
            model_name='academicunit',
            name='schoolOf',
            field=models.ForeignKey(db_column='facultad', on_delete=django.db.models.deletion.CASCADE, to='organization.schoolof'),
        ),
    ]
