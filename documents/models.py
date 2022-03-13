from django.db import models


class DocumentType(models.Model):
    name = models.CharField(max_length=100, db_column='nombre')
    description = models.CharField(max_length=100, db_column='descripcion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'doc_tipo_documento'


class Area(models.Model):
    name = models.CharField(max_length=100, db_column='nombre')
    description = models.CharField(max_length=100, db_column='descripcion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'doc_area'


class Category(models.Model):
    name = models.CharField(max_length=100, db_column='nombre')
    description = models.CharField(max_length=100, db_column='descripcion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'doc_categoria'


class LevelAccess(models.Model):
    name = models.CharField(max_length=100, db_column='nombre')
    description = models.CharField(max_length=100, db_column='descripcion')
    state = models.BooleanField(default=True, db_column='estado')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'doc_nivel_acceso'


class Document(models.Model):
    name = models.CharField(max_length=100, db_column='nombre')
    description = models.CharField(max_length=100, db_column='descripcion')
    electronicSignature = models.BooleanField(default=True, db_column='firma_electronica')
    manualSignature = models.BooleanField(default=True, db_column='firma_manual')
    create_date = models.DateTimeField(auto_now=True, db_column='fecha_creacion')
    pathFile = models.FileField(upload_to='files/documents', max_length=10000, db_column='ruta_archivo')
    state = models.BooleanField(default=True, db_column='estado')
    category = models.ForeignKey(Category, db_column='id_categoria', on_delete=models.CASCADE)
    level_access = models.ForeignKey(LevelAccess, db_column='id_nivel_acceso', on_delete=models.CASCADE)
    documentType = models.ForeignKey(DocumentType, db_column='id_documento', on_delete=models.CASCADE)
    area = models.ForeignKey(Area, db_column='id_area', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'name'
        db_table = 'doc_documento'
