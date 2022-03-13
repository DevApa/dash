from django.db import models

from authentication.models import Usuario


class Frequency(models.Model):
    name = models.CharField(max_length=100, unique=True, db_column='nombre')
    description = models.CharField(max_length=100, unique=True, db_column='descripcion')
    state = models.BooleanField(default=False, db_column='estado')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.name)

    class Meta:
        db_table = 'inv_frecuencia'


class Capacity(models.Model):
    name = models.CharField(max_length=100, unique=True, db_column='nombre')
    description = models.CharField(max_length=100, unique=True, db_column='descripcion')
    state = models.BooleanField(default=False, db_column='estado')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')

    def __str__(self):
        txt = '{0} '
        return txt.format(self.name)

    class Meta:
        db_table = 'inv_capacidad'


class Brand(models.Model):
    name = models.CharField(max_length=60, unique=True, db_column='nombre')
    description = models.CharField(max_length=60, unique=True, db_column='descripcion')
    state = models.BooleanField(default=True, db_column='estado')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'inv_marca'


class EModel(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False, unique=True, db_column='nombre')
    description = models.CharField(max_length=100, null=False, blank=False, unique=True, db_column='Descripcion')
    state = models.BooleanField(default=True, db_column='estado')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.name)

    class Meta:
        db_table = 'inv_modelo'


class Location(models.Model):
    name = models.CharField(db_column='nombre', max_length=255)
    description = models.CharField(db_column='description', max_length=255)
    state = models.BooleanField(default=True, db_column='estado')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.name)

    class Meta:
        db_table = 'inv_ubicacion'


class Generation(models.Model):
    name = models.CharField(db_column='nombre', max_length=255)
    description = models.CharField(db_column='description', max_length=255)
    state = models.BooleanField(default=True, db_column='estado')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')

    def __str__(self):
        txt = "{0} "
        return txt.format(self.name)

    class Meta:
        db_table = 'inv_generacion'


class FileSystem(models.Model):
    name = models.CharField(db_column='nombre', max_length=255)
    description = models.CharField(db_column='description', max_length=255)
    state = models.BooleanField(default=True, db_column='estado')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')

    class Meta:
        db_table = 'inv_archivo_sistema'


class ItemType(models.Model):
    code = models.CharField(db_column='codigo', max_length=255)
    description = models.CharField(db_column='description', max_length=255)
    state = models.BooleanField(default=True, db_column='estado')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')

    class Meta:
        db_table = 'inv_tipo_item'


class TransactionType(models.Model):
    code = models.CharField(db_column='codigo', max_length=255)
    description = models.CharField(db_column='description', max_length=255)
    state = models.BooleanField(default=True, db_column='estado')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')

    class Meta:
        db_table = 'inv_tipo_transaccion'


class TransactionReason(models.Model):
    type_trx = models.ForeignKey(TransactionType, db_column='id_tipo_trx', on_delete=models.CASCADE)
    description = models.CharField(db_column='description', max_length=255)
    date_created = models.DateTimeField(db_column='fecha_creacion', auto_now_add=True,)

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'inv_motivo_transaccion'


class EquipmentType(models.Model):
    code = models.CharField(db_column='codigo', max_length=255)
    description = models.CharField(db_column='description', max_length=255)
    state = models.BooleanField(default=True, db_column='estado')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')

    class Meta:
        db_table = 'inv_tipo_equipo'


class Equipment(models.Model):
    code = models.CharField(db_column='codigo', max_length=255)
    description = models.CharField(db_column='description', max_length=255)
    employee_id = models.ForeignKey(Usuario, db_column='id_usuario', on_delete=models.CASCADE)
    eq_type = models.ForeignKey(EquipmentType, db_column='id_tipo_equipo', on_delete=models.CASCADE)
    state = models.BooleanField(default=True, db_column='estado')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')

    class Meta:
        db_table = 'inv_equipo'


class EquipmentTrx(models.Model):
    code = models.CharField(db_column='codigo', max_length=255)
    description = models.CharField(db_column='description', max_length=255)
    employee_id = models.ForeignKey(Usuario, db_column='id_usuario', on_delete=models.CASCADE)
    eq_type = models.ForeignKey(EquipmentType, db_column='id_tipo_equipo', on_delete=models.CASCADE)
    state = models.BooleanField(default=True, db_column='estado')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')

    class Meta:
        db_table = 'inv_transaccion_equipo'


class Item(models.Model):
    description = models.TextField(ItemType, db_column='description', max_length=255)
    employee_id = models.ForeignKey(Brand, db_column='id_empleado', on_delete=models.CASCADE)
    eq_type = models.ForeignKey(EModel, db_column='id_tipo_equipo', on_delete=models.CASCADE)
    location_id = models.ForeignKey(Location, db_column='id_ubicacion', on_delete=models.CASCADE)
    generation_id = models.ForeignKey(Generation, db_column='id_generacion', on_delete=models.CASCADE)
    capacity_id = models.ForeignKey(Capacity, db_column='id_capacidad', on_delete=models.CASCADE)
    frequency_id = models.ForeignKey(Frequency, db_column='id_frecuencia', on_delete=models.CASCADE)
    state = models.BooleanField(default=True, db_column='estado')
    quantity = models.IntegerField(db_column='cantidad')
    value = models.IntegerField(db_column='valor')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')

    class Meta:
        db_table = 'inv_item'


class Inventory(models.Model):
    code = models.CharField(db_column='codigo', max_length=255)
    description = models.CharField(db_column='description', max_length=255)
    state = models.BooleanField(default=True, db_column='estado')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    date_update = models.DateTimeField(auto_now=True, db_column='fecha_edicion')

    class Meta:
        db_table = 'inv_inventario'


class HardwareEquipmentDetail(models.Model):
    serie = models.TextField(db_column='serie', max_length=255)
    item_id = models.ForeignKey(Item, db_column='id_item', on_delete=models.CASCADE)
    equipment_id = models.ForeignKey(Equipment, db_column='id_equipo', on_delete=models.CASCADE)
    inventory_id = models.ForeignKey(Inventory, db_column='id_inventario', on_delete=models.CASCADE)
    state = models.BooleanField(default=True, db_column='estado')
    date_created = models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')
    quantity = models.IntegerField(db_column='cantidad')
    observation = models.TextField(db_column='observacion')

    class Meta:
        db_table = 'inv_equipo_detalle_hardware'


class Partition(models.Model):
    eq_detail_id = models.ForeignKey(HardwareEquipmentDetail, db_column='id_equipo_detalle_hardware', on_delete=models.CASCADE)
    name = models.TextField(db_column='nombre', max_length=255)
    capacity = models.DecimalField(max_digits=5, decimal_places=2, db_column='capacidad')
    free_space = models.DecimalField(max_digits=5, decimal_places=2, db_column='espacio_libre')
    file_sys = models.ForeignKey(FileSystem,db_column='id_file_system', on_delete=models.CASCADE)
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'inv_particion'


class Software(models.Model):
    name = models.TextField(db_column='nombre', max_length=255)
    published_by = models.TextField(db_column='publicado_por', max_length=255)
    install_date = models.DateField(db_column='fecha_instalacion')
    version = models.TextField(db_column='version', max_length=100)
    link_support = models.TextField(db_column='link_soporte', max_length=500)
    link_help = models.TextField(db_column='link_ayuda', max_length=500)
    link_update = models.TextField(db_column='link_actualizacion', max_length=500)
    comment = models.TextField(db_column='comentario', max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'inv_software'

