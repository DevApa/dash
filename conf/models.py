from django.db import models


class Rol(models.Model):
    descripcion = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return f'{self.descripcion}'

    class Meta:
        db_table = 'sec_rol'


class Modulo(models.Model):
    descripcion = models.TextField(max_length=1000)
    orden = models.IntegerField(default=0)
    icon = models.TextField(max_length=1000)
    key = models.TextField(max_length=1000)
    menus = []

    def __str__(self):
        return f'{self.descripcion}'

    class Meta:
        db_table = 'sec_modulo'
        ordering = ('orden',)


class Menu(models.Model):
    descripcion = models.TextField(max_length=1000)
    orden = models.IntegerField(default=0)
    icon = models.TextField(max_length=1000, null=True)
    href = models.TextField(max_length=1000, null=True)
    url = models.TextField(max_length=1000, null=True)
    modulo_id = models.ForeignKey(Modulo, on_delete=models.SET_NULL, null=True)
    parent_id = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)
    roles = models.ManyToManyField(Rol, blank=False, through='RolMenu')
    key = models.TextField(max_length=1000, null=True)
    items = []

    def __str__(self):
        return f'{self.descripcion}'

    class Meta:
        db_table = 'sec_menu'
        ordering = ('orden',)


class Icono(models.Model):
    descripcion = models.TextField(max_length=1000, null=True)

    class Meta:
        db_table = 'sec_icono'


class RolMenu(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    rol = models.ForeignKey(Rol, on_delete=models.SET_NULL, null=True)
    descripcion = models.TextField(max_length=1000, null=True)

    def __str__(self):
        return f'{self.descripcion}'

    class Meta:
        db_table = 'sec_rol_menu'
