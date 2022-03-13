from django.db import models

from authentication.models import Usuario
from organization.choices import tipos


class University(models.Model):
    name = models.TextField(max_length=300, null=False, blank=False, unique=True, db_column='nombre')
    address = models.TextField(max_length=1000, null=True, blank=True, db_column='direccion')
    phone = models.TextField(max_length=30, null=True, blank=True, db_column='telefono')
    rector = models.TextField(max_length=300, null=True, db_column='rector')
    type = models.TextField(max_length=1000, choices=tipos, null=True, db_column='tipo')
    foundation_date = models.DateField(db_column='fecha_fundacion')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')
    date_input = models.TextField(max_length=5, null=True, db_column='hora_ingreso')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'org_universidad'


class SchoolOf(models.Model):
    university = models.ForeignKey(University, db_column='univeridad', on_delete=models.CASCADE)
    name = models.TextField(max_length=300, null=False, blank=False, unique=True, db_column='nombre')
    address = models.TextField(max_length=1000, null=True, db_column='direccion')
    phone = models.TextField(max_length=30, null=True, db_column='telefono')
    dean = models.TextField(max_length=300, null=True, db_column='decano')
    foundation_date = models.DateField(db_column='fecha_fundacion')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')
    date_input = models.TextField(max_length=5, null=True, db_column='hora_ingreso')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'org_facultad'


class AcademicUnit(models.Model):
    name = models.TextField(max_length=300, null=False, blank=False, unique=True, db_column='nombre')
    address = models.TextField(max_length=1000, null=True, db_column='direccion')
    phone = models.TextField(max_length=30, null=True, db_column='telefono')
    director = models.TextField(max_length=300, null=True, db_column='director')
    foundation_date = models.DateField(db_column='fecha_fundacion')
    schoolOf = models.ForeignKey(SchoolOf, db_column='facultad', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')
    date_input = models.TextField(max_length=5, null=True, db_column='hora_ingreso')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'org_unidad_Academica'


class Department(models.Model):
    name = models.CharField(max_length=50, db_column='nombre')
    phone = models.TextField(max_length=30, null=True, db_column='telefono')
    boss = models.ForeignKey(Usuario, db_column='jefe', on_delete=models.CASCADE)
    foundation_date = models.DateField(db_column='fecha_fundacion')
    academic_unit = models.ForeignKey(AcademicUnit, db_column='unidad_academica', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')
    date_input = models.TextField(max_length=5, null=True, db_column='hora_ingreso')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'name'
        db_table = 'org_departamento'

